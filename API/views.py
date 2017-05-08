from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.

class CustomerListesi(APIView):

    def get(self, request):
        kurlar = Customer.objects.all()
        serializer = CustomerSerializer(kurlar, many=True)
        return  Response(serializer.data)

    def post(self):
        pass