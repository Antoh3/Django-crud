from rest_framework.serializers import ModelSerializer
from .models import Crud



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Crud
        fields = '__all__'