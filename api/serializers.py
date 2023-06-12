from rest_framework import serializers
from django.utils import timezone

from .models import MyModel, Standard, Company


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate_founded_date(self, value):

        if value > timezone.now().date():
            raise serializers.ValidationError(
                "Founded date cannot be in the future.")
        return value

    def validate_name(self, value):

        min_length = 3
        if len(value) < min_length:
            raise serializers.ValidationError(
                f"Name must be at least {min_length} characters long.")
        return value


class OtpSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6, required=False)