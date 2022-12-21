from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Pagos(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    monto = models.FloatField(default=0.0)

class Services(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    logo = models.CharField(max_length=300)

class Expired_payments(models.Model):
    payment_user_id = models.ForeignKey(User, on_delete =models.CASCADE, related_name='expired_payments_users')
    penalty_fee_amount = models.FloatField(default=0.0)

class Payment_user(models.Model):
    user_id = models.ForeignKey(User, on_delete =models.CASCADE, related_name='payment_users')
    service_id = models.ForeignKey(Services, on_delete =models.CASCADE, related_name='services')
    amount = models.FloatField(default=0.0)
    payment_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        
        if self.expiration_date < self.payment_date:
            Expired_payments.create(payment_user_id = self.user_id,  penalty_fee_amount = 30)

        super().save(*args, **kwargs)