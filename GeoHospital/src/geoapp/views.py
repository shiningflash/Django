from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, Point
from django.contrib.gis.measure import D
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status, views
# import django_filters.rest_framework
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework_gis.filters import DistanceToPointOrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Hospital
from .serializers import HospitalSerializer


class HospitalView(views.APIView):
    
    def get(self, request):
        queryset = Hospital.objects.all()
        serializer = HospitalSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class HospitalDetails(views.APIView):
    
    def get(self, request, pk):
        try:
            hospital = Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            return Response('Hospital not found', status=status.HTTP_404_NOT_FOUND)
        
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            hospital = Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            return Response('Hospital not found', status=status.HTTP_404_NOT_FOUND)
        
        data = JSONParser().parse(request)
        serializer = HospitalSerializer(hospital, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response('Hospital info updated', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            hospital = Hospital.objects.get(pk=pk)
            hospital.delete()
            return Response('Hospital deleted', status=status.HTTP_204_NO_CONTENT)
        except Hospital.DoesNotExist:
            return Response('Hospital not found', status=status.HTTP_404_NOT_FOUND)
         

class HospitalList(generics.ListAPIView):
    serializer_class = HospitalSerializer
    
    def get_queryset(self):
        queryset = Hospital.objects.all()
        name = self.request.query_params.get('name', None)
        
        if name is not None:
            queryset = queryset.filter(name__contains = name)
        return queryset


# point to lat, long
# point = models.PointField()
# lat = point.x
# long = point.y

# lat long to Point
# location = Point(long, lat, srid=4326)


class SearchHospital(views.APIView):
    # Location of Square Hospital
    latitude = 23.7532
    longitude = 90.3817
    
    # Mohakhali, Near my house
    # latitude = 23.7800
    # longitude = 90.4102
    
    my_location = Point(latitude, longitude, srid=4326)
    model = Hospital
    context_object_name = 'hospital'
    
    def get(self, request):
        # all hospitals within 500 m
        # queryset = Hospital.objects.filter(location__distance_lte=(self.my_location, D(m=500)))
        
        # 5 hospital near my location (order by ascending distance)
        # queryset = Hospital.objects.annotate(distance = Distance('location', self.my_location)).order_by('distance')[0:5]
        
        # al most 5 hospital, within 500 m, and order by ascending distance
        # queryset = Hospital.objects.annotate(distance = Distance('location', self.my_location)).filter(location__distance_lte=(self.my_location, D(m=5000))).order_by('distance')[0:5]
        
        # check specific hospital of a specific location
        queryset = Hospital.objects.filter(location=self.my_location)
        
        serializer = HospitalSerializer(queryset, many=True)
        return Response(serializer.data)