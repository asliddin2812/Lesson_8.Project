from rest_framework import serializers
from .models import OmonimTafsiloti, Omonimlar

class OmonimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omonimlar
        fields = '__all__'


class OmonimlarTafsilotiSerializer(serializers.ModelSerializer):
    omonim = serializers.PrimaryKeyRelatedField(queryset=Omonimlar.objects.all())

    class Meta:
        model = OmonimTafsiloti
        fields = '__all__'
        read_only_fields = ('id',)
