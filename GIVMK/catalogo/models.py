from crum import get_current_user
from django.db import models
from django.forms.models import model_to_dict

from GIVMK.settings import MEDIA_URL, STATIC_URL

from core.models import Base

# Create your models here.


''' * Importacion que nos permite maquetar o formatear
con HTML una variable o texto para poder mostrar en el admin*'''
from django.utils.html import format_html

# Librerias de importacion de PILLOW para poder
# mostrar thubnails de las imagenes subidas al sistema*'''
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Impotamos Mark_Safe para poder mostar la img en el Admin
from django.utils.safestring import mark_safe


# Metodo para eliminar una fotografia si ya existe
# en la base de datos y evitar llenar el especio '''
def custom_upload_to(instance, filename):
    '''Este metodo elimina de nuestra base de datos una imagen
    de una instancia se esta ya tenia una imagen previa'''
    # Obtiene la imagen antigua de la instancia en cuestion
    old_instance = Producto.objects.get(pk=instance.pk)
    # Borra la imagen de la que se ha seleccionado
    old_instance.foto.delete()
    return 'Catalogo/Producto' + filename


class Producto(Base):
    nombre = models.CharField('Nombre', max_length=125)
    precio_consultora = models.DecimalField('Precio Consultora', max_digits=7, decimal_places=2)
    precio_catalogo = models.DecimalField('Precio Catalogo', max_digits=7, decimal_places=2)
    descripcion = models.TextField('Decripción', blank=True, null=True)
    img = models.ImageField(
        upload_to='Catalogo/', null=True, blank=True, verbose_name='Imagen')
    estado = models.BooleanField('Estado', default=False, editable=False)

    # campo que creara la imagen en thubnail
    img_thubmnail = ImageSpecField(
        source='img',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 60})

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def toJSON(self):
        item = model_to_dict(self, exclude=['img_thubmnail', 'img'])
        # item['nombre'] = self.nombre
        item['precio_consultora'] = format(self.precio_consultora, '.2f')
        item['precio_catalogo'] = format(self.precio_catalogo, '.2f')
        item['cantidad'] = int(self.existencia())
        item['invertido_cons'] = self.calcularMontoCosto()
        item['invertido_cat'] = self.calcularMontoVenta()
        # item['img_thubmnail'] = self.img_thubmnail
        item['img'] = self.get_img()
        item['existencia'] = int(self.existencia())
        return item

    def existencia(self):
        # from inventario.models import Ingreso, IngresoDetalle
        # from ventas.models import VentaDetalle
        cantidad = 0
        # Sumamos los ingresos a el inventario
        # for ingreso in IngresoDetalle.objects.filter(id_producto=self.id):
        #     cantidad += ingreso.cantidad
        # # Restamos las ventas
        # # for salida in VentaDetalle.objects(id_producto=self.id):
        # #     cantidad -= salida.cantidad
        # if VentaDetalle.objects.filter(id_producto=self.id):
        #     for venta in VentaDetalle.objects.filter(id_producto=self.id):
        #         cantidad -= venta.cantidad
        # if cantidad == 0:
        #     self.estado = False
        return cantidad

    def existenciaColor(self):
        cantidad = self.existencia()
        if cantidad == 0:
            cantidad = '--'
            color1 = '#D7142B'
            color2 = '#FF7800'
        else:
            self.estado = True
            if cantidad <= 1:
                color1 = '#D7142B'
                color2 = "#FF7800"
            elif cantidad <= 5:
                color1 = '#FF7800'
                color2 = 'yellow'
            else:
                color1 = '#009A19'
                color2 = '#8AFF00'
        self.save()
        return format_html(
            '<span style="color:' + color1 + '; font-weight: bold;' +
            ' text-shadow: 0px 0px 2px ' + color2 + ';">' +
            str(cantidad) + '</span>')

    # Sirve para mostrar la descripcion del metodo en el ADMIN
    existenciaColor.short_description = 'Existencias'

    def calcularMontoCosto(self):
        # from inventario.models import Ingreso, IngresoDetalle
        monto = 0
        # for producto in IngresoDetalle.objects.filter(id_producto=self.id):
        #     monto = monto + producto.monto_costo()
        if monto == 0:
            monto = '--'
            color1 = '#D7142B'
            color2 = '#FF7800'
        else:
            color1 = '#009A19'
            color2 = '#8AFF00'

        return format_html(
            '<span style="color:' + color1 + '; font-weight: bold;' +
            ' text-shadow: 0px 0px 2px ' + color2 + ';">Q. ' +
            str(monto) + '</span>')

    calcularMontoCosto.short_description = 'Monto Costo Inventario'

    def calcularMontoVenta(self):
        # from inventario.models import Ingreso, IngresoDetalle
        monto = 0
        # for producto in IngresoDetalle.objects.filter(id_producto=self.id):
        #     monto = monto + producto.monto_venta()
        if monto == 0:
            monto = '--'
            color1 = '#D7142B'
            color2 = '#FF7800'
        else:
            color1 = '#009A19'
            color2 = '#8AFF00'

        return format_html(
            '<span style="color:' + color1 + '; font-weight: bold;' +
            ' text-shadow: 0px 0px 2px ' + color2 + ';">Q. ' +
            str(monto) + '</span>')

    calcularMontoVenta.short_description = 'Monto Venta Inventario'

    def get_img(self):
        if self.img_thubmnail:
            return '{}{}'.format(MEDIA_URL, self.img_thubmnail)
        return '{}{}'.format(STATIC_URL, 'core/img/image-not.jpg')

    def image_thub(self):
        ''' Retornara una imagen para ser mostrada en al admin
        en el catalogo del mismo, si no la encuetra coloca otra por default'''
        # Valida si se le subio imagen al material
        if self.img_thubmnail:
            # Y lo retorna en la lista de materiales
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=self.img_thubmnail.url, width=50, height=50, ))
        # Si no encuentra mostrar una imagen generica
        else:
            # Y lo retorna en la lista de materiales
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url='/../static/core/img/no-img.jpg', width=50, height=50, ))

    # Sirve para mostrar la descripcion del metodo en el ADMIN
    image_thub.short_description = 'Imagen'

    def __str__(self):
        return '%s %s Exsitencias: %s' % (self.nombre, self.precio_catalogo, self.existencia())