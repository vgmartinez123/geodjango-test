from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import PolygonPoints


class PolygonPointsSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = PolygonPoints
        fields = '__all__'
        geo_field = 'geom'
