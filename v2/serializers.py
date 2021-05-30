from rest_framework import serializers
from .models import *

class ProfessionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    type = serializers.CharField()
    icon = serializers.CharField()
    description = serializers.CharField()
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Profession.objects.create(**validated_data)

class RaidSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    addon = serializers.CharField()
    img = serializers.CharField()
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Raid.objects.create(**validated_data)

class HeroClassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    img = serializers.CharField()
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return HeroClass.objects.create(**validated_data)

class RaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    fraction = serializers.CharField()
    img = serializers.CharField()
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Race.objects.create(**validated_data)


# class ProfessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profession
#         fields = ['id', 'name', 'type', 'icon', 'description']
