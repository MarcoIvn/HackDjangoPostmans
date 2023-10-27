from django.db import models

class Crime(models.Model):
    ID = models.AutoField(primary_key=True)
    Año = models.IntegerField()
    Clave_Ent = models.CharField(max_length=4)
    Entidad = models.CharField(max_length=255)
    Bien_juridico_afectado = models.CharField(max_length=255)
    Tipo_de_delito = models.CharField(max_length=255)
    Subtipo_de_delito = models.CharField(max_length=255)
    Modalidad = models.CharField(max_length=255)
    Enero = models.IntegerField()
    Febrero = models.IntegerField()
    Marzo = models.IntegerField()
    Abril = models.IntegerField()
    Mayo = models.IntegerField()
    Junio = models.IntegerField()
    Julio = models.IntegerField()
    Agosto = models.IntegerField()
    Septiembre = models.IntegerField()
    Octubre = models.IntegerField()
    Noviembre = models.IntegerField()
    Diciembre = models.IntegerField()
    Sexo_Averiguacion_previa = models.CharField(max_length=255)
    Rango_de_edad = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Año} - {self.Entidad} - {self.Tipo_de_delito}"
