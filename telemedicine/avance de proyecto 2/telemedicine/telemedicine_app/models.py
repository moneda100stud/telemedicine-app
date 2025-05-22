from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return self.name
