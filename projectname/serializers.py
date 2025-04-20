from rest_framework import serializers
from .models import File
from django.contrib.auth.models import User

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


...

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            )

        user.set_password(validated_data['password'])
        user.save()
        return user