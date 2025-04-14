from rest_framework import serializers
from .models import File

class Fileserializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'