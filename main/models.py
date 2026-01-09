from django.db import models

# Create your models here.

#site olympique
class Olympiade(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Typologie(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom


class Denomination(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class DateReference(models.Model):
    valeur = models.CharField(max_length=10)
    def __str__(self):
        return self.valeur

class Site(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    adresse = models.CharField(max_length=255, blank=True)
    commune = models.CharField(max_length=100)
    departement = models.IntegerField()
    code_postal = models.CharField(max_length=10)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    url_image = models.URLField(blank=True)
    credits = models.CharField(max_length=255, blank=True)
    datation = models.CharField(max_length=255, blank=True)

    olympiade = models.ForeignKey(
        "Olympiade",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    typologies = models.ManyToManyField("Typologie", blank=True)
    denominations = models.ManyToManyField("Denomination", blank=True)
    dates_reference = models.ManyToManyField("DateReference", blank=True)

    def __str__(self):
        return self.nom