from django.urls import path
from .views import StudentDetailView,StudentsListCreatView



urlpatterns =[
    path('students/',StudentsListCreatView.as_view()),
    path('students/<int:pk>/',StudentDetailView.as_view())
]