from django.db import models
from rest_framework import fields, serializers

from .models import AddBooks

class AddBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBooks
        fields = '__all__'
