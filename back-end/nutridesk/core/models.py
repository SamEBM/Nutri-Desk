from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class InfoUsuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.DO_NOTHING,verbose_name='Usuario',null=False,blank=False,)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", default=datetime.now)
    altura = models.FloatField(verbose_name="Altura en CM")
    peso = models.FloatField(verbose_name="Peso en KG")
    SEXOS = (
        ('H','Hombre'),
        ('M','Mujer'),
    )
    sexo = models.CharField(max_length=1, choices=SEXOS)

    class Meta:
        ordering = ('-usuario',)

    def __str__(self):
        return '{0} - {1} {2}'.format(self.usuario.username, self.usuario.first_name, self.usuario.last_name)