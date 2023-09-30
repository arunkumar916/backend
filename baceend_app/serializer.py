from rest_framework import serializers
from .models import Enroll
class EnrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = '__all__'