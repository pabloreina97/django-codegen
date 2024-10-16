from rest_framework import serializers
from .models import Trabajador

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ['gpt_auto_generate']