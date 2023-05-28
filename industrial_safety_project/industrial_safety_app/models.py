from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    temperature = models.IntegerField("temperature")
    pressure = models.IntegerField("pressure")
    mass = models.IntegerField("mass")
    voltage = models.IntegerField("voltage")
    resistance = models.IntegerField("resistance")
    temperature1 = models.IntegerField("temperature1")
    pressure1 = models.IntegerField("pressure1")
    datetime = models.DateTimeField('datetime')

    def __str__(self):
        return self.id
