from django.db import models


class Dummy(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Geo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=128)


class GeoGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(Dummy, related_name='geo_groups')
    geos = models.ManyToManyField(Geo, related_name='geo_groups')

    def __str__(self):
        return self.name
