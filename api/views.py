from django.shortcuts import render
from rest_framework import generics
from .serializer import StudentSerializer
from .models import Crud


class StudentsListCreatView(generics.ListCreateAPIView):
    queryset = Crud.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crud.objects.all()
    serializer_class = StudentSerializer
