from django.shortcuts import render
from rest_framework import generics
from .serializer import StudentSerializer
from .models import Student


class ListCreateStudent(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DetailViewStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer