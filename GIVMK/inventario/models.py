from django.db import models
from core.models import Base
from crum import get_current_user # Agrega al Usuario de la clase CRUM
from django.forms import model_to_dict # Convierte una clase a Diccionario
from catalogo.models import Producto
from django.utils.html import format_html # Formatea un dato con html
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

class Pedido(Base):
    fecha = models.DateField('Fecha de Ingreso')
    referencia = models.CharField(
        'Referencia de Pedido', max_length=150, blank=True, null=True,
        help_text='La referncia puede ser un dato de descripcion del porque realiza el pedido')
    totalConsultora = models.DecimalField(
        'Total Consultora', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00)
    totalCatalogo = models.DecimalField(
        'Total Catalogo', max_digits=12, decimal_places=2, null=True, blank=True, default=0.00)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.dateCreate
        item['totalConsultora'] = format(self.totalConsultora, '.2f')
        item['totalCatalogo'] = format(self.totalCatalogo, '.2f')
        item['ganancia'] = format((self.totalCatalogo - self.totalConsultora), '.2f')
        item['cantidadProd'] = self.contProds()
        return item

    def __str__(self):
        return '%s %s' % (self.dateCreate, self.referencia)

    def contProds(self):
        total = 0
        for det in DetallePedido.objects.filter(pedido_id=self.id):
            total += det.cantidad
        return total

class DetallePedido(Base):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,
        verbose_name='Producto')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,
        verbose_name='Pedido')
    pConsultora = models.DecimalField(
        'Precio Consultora', max_digits=12, decimal_places=2,
        help_text='Precio al que lo compra la consultora')
    pCatalogo = models.DecimalField(
        'Precio Catalogo', max_digits=12, decimal_places=2,
        help_text='Precio al que se vendera el producto')
    cantidad = models.PositiveIntegerField(
        'Cantidad')

    class Meta:
        verbose_name = "Detalle de Pedidos"
        verbose_name_plural = "Detalles de Pedidos"

    def __str__(self):
        return '%s %s' % (self.pedido, self.producto)

    def toJSON(self):
        item = model_to_dict(self)
        item['producto'] = self.producto.toJSON()
        item['pConsultora'] = format(self.pConsultora, '.2f')
        item['pCatalogo'] = format(self.pCatalogo, '.2f')
        item['subConsultora'] = format(self.subTotalConsultora(), '.2f')
        item['subCatalogo'] = format(self.subTotalCatalogo(), '.2f')
        return item

    def subTotalConsultora(self):
        total = self.pConsultora * self.cantidad
        return float(total)

    def subTotalCatalogo(self):
        total = self.pCatalogo * self.cantidad
        return float(total)