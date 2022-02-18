from django.db.models import fields
from rest_framework.utils import model_meta
from .models import Model_Forms
from rest_framework import serializers

class Model_FormsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model_Forms
        fields = '__all__'