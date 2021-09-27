from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, Point
from rest_framework.decorators import action
from django_filters import rest_framework as filters
# from . polygon_filters import PolygonPointsFilter
from . models import PolygonPoints
from . serializers import PolygonPointsSerializer


class PolygonPointsViewSet(viewsets.ModelViewSet):
    serializer_class = PolygonPointsSerializer
    queryset = PolygonPoints.objects.all()
    # filterset_class = PolygonPointsFilter
    filter_backends = [filters.DjangoFilterBackend]

    @action(detail=False, methods=['get'])
    def get_nearest_facilities(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords), srid=4326)
            # nearest_five_facilities = PolygonPoints.objects.annotate(
            #     distance=Distance('geom', user_location)).order_by('distance')[:5]
            is_inside = self.PolygonPoints.geofence.contains(user_location)
            # serializer = self.get_serializer_class()
            # serialized = serializer(nearest_five_facilities, many=True)
            print(is_inside)
            return Response(is_inside, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
