from django.db import models


class District(models.Model):
    name = models.CharField(
        max_length=150,
    )
    bn_name = models.CharField(max_length=150, null=False, blank=False)
    lat = models.FloatField(null=False, blank=False)
    lon = models.FloatField(null=False, blank=True)

    class Meta:
        indexes = [models.Index(fields=["name", "lat", "lon"])]

    def __str__(self) -> str:
        return self.name
