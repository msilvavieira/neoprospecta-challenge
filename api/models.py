from django.db import models



class Entry(models.Model):
    access_id = models.CharField(max_length=100, unique=True)
    kingdom = models.ForeignKey('Kingdom', on_delete=models.CASCADE)
    species = models.ForeignKey('Species', on_delete=models.CASCADE)
    sequence = models.CharField(max_length=100)

    def __str__(self):
        return ' - '.join([self.access_id, self.kingdom.label, self.species.label, self.sequence])

    class Meta:
        ordering = ('access_id',)

class Kingdom(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Species(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

