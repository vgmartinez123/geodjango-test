from django.db import models
from django.contrib.gis.db import models


class PolygonPoints(models.Model):
    # PointField is a field of points
    # Point is an (x, y) coordinate point, could be used to store lon and lat in our case
    geom = models.PointField(default=None, blank=True, null=True)
    data = models.JSONField(default=dict)

    class Meta:
        managed = False
        db_table = 'polygon_points'
