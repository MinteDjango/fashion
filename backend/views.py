from django.shortcuts import render
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.views import APIView
from fashiongebeya.models import Item
from .serializers import ItemSerializer

class Items(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["caption", "brand", "price", "what"]

class ItemSearch(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["caption", "brand", "what", "price"]

class Trending(generics.ListAPIView):
    queryset = Item.objects.filter(trending=True)
    serializer_class = ItemSerializer

class ims(APIView):
    def get(*args, **kwargs):
        data = Item.objects.all()
        serializer = ItemSerializer(data=data, many=True)
        return Response(serializer.data)
