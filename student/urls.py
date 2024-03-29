from django.urls import path
from .views import DetailViewStudent,ListCreateStudent



urlpatterns =[
    path('student/',ListCreateStudent.as_view()),
    path('student/<int:pk>/',DetailViewStudent.as_view()),
]