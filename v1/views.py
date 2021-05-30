#from django.shortcuts import render
# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class ProfessionsView(APIView):
    def get_queryset(self):
        return self.request.query_params.get('type')

    def get(self, request):
        professions = Profession.objects.all()
        profession_type = self.get_queryset()

        if profession_type is not None:
            professions = professions.filter(type=profession_type)

        serializer = ProfessionSerializer(professions, many=True)
        return Response({"professions": serializer.data})

    def post(self, request):
        profession = request.data.get('profession')
        serializer = ProfessionSerializer(data=profession)
        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()
        return Response({"success": profession_saved.id})
    
class ProfessionView(APIView):
    def get(self, request, pk):
        profession = get_object_or_404(Profession.objects.all(), pk=pk)
        serializer = ProfessionSerializer(profession)
        return Response({"profession": serializer.data})

    def delete(self, request, pk):
        profession = get_object_or_404(Profession.objects.all(), pk=pk)
        profession.delete()
        return Response({
            "success": pk
        }, status=204)

    def put(self, request, pk):
        saved_profession = get_object_or_404(Profession.objects.all(), pk=pk)
        data = request.data.get('profession')
        serializer = ProfessionSerializer(instance=saved_profession, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()
        return Response({
            "success": profession_saved.id
        })

####

class RaidsView(APIView):
    def get_queryset(self):
        return self.request.query_params.get('addon')

    def get(self, request):
        raids = Raid.objects.all()
        raid_addon = self.get_queryset()

        if raid_addon is not None:
            raids = raids.filter(addon=raid_addon)
        serializer = RaidSerializer(raids, many=True)
        return Response({"raids": serializer.data})

    def post(self, request):
        raid = request.data.get('raid')
        serializer = RaidSerializer(data=raid)
        if serializer.is_valid(raise_exception=True):
            raid_saved = serializer.save()
        return Response({"success": raid_saved.id})
    
class RaidView(APIView):
    def get(self, request, pk):
        raid = get_object_or_404(Raid.objects.all(), pk=pk)
        serializer = RaidSerializer(raid)
        return Response({"raid": serializer.data})

    def delete(self, request, pk):
        raid = get_object_or_404(Raid.objects.all(), pk=pk)
        raid.delete()
        return Response({
            "success": pk
        }, status=204)

    def put(self, request, pk):
        saved_raid = get_object_or_404(Raid.objects.all(), pk=pk)
        data = request.data.get('raid')
        serializer = RaidSerializer(instance=saved_raid, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            raid_saved = serializer.save()
        return Response({
            "success": raid_saved.id
        })

###

class HeroClassesView(APIView):
    def get(self, request):
        heroClasses = HeroClass.objects.all()
        serializer = HeroClassSerializer(heroClasses, many=True)
        return Response({"heroClasses": serializer.data})

    def post(self, request):
        heroClass = request.data.get('heroClass')
        serializer = HeroClassSerializer(data=heroClass)
        if serializer.is_valid(raise_exception=True):
            heroClass_saved = serializer.save()
        return Response({"success": heroClass_saved.id})
    
class HeroClassView(APIView):
    def get(self, request, pk):
        heroClass = get_object_or_404(HeroClass.objects.all(), pk=pk)
        serializer = HeroClassSerializer(heroClass)
        return Response({"heroClass": serializer.data})

    def delete(self, request, pk):
        heroClass = get_object_or_404(HeroClass.objects.all(), pk=pk)
        heroClass.delete()
        return Response({
            "success": pk
        }, status=204)

    def put(self, request, pk):
        saved_heroClass = get_object_or_404(HeroClass.objects.all(), pk=pk)
        data = request.data.get('heroClass')
        serializer = HeroClassSerializer(instance=saved_heroClass, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            heroClass_saved = serializer.save()
        return Response({
            "success": heroClass_saved.id
        })

###

class RaciesView(APIView):
    def get_queryset(self):
        return self.request.query_params.get('fraction')

    def get(self, request):
        racies = Race.objects.all()
        race_fraction = self.get_queryset()

        if race_fraction is not None:
            racies = racies.filter(fraction=race_fraction)
        serializer = RaceSerializer(racies, many=True)
        return Response({"racies": serializer.data})

    def post(self, request):
        race = request.data.get('race')
        serializer = RaceSerializer(data=race)
        if serializer.is_valid(raise_exception=True):
            race_saved = serializer.save()
        return Response({"success": race_saved.id})
    
class RaceView(APIView):
    def get(self, request, pk):
        race = get_object_or_404(Race.objects.all(), pk=pk)
        serializer = RaceSerializer(race)
        return Response({"race": serializer.data})

    def delete(self, request, pk):
        race = get_object_or_404(Race.objects.all(), pk=pk)
        race.delete()
        return Response({
            "success": pk
        }, status=204)

    def put(self, request, pk):
        saved_race = get_object_or_404(Race.objects.all(), pk=pk)
        data = request.data.get('race')
        serializer = RaceSerializer(instance=saved_race, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            race_saved = serializer.save()
        return Response({
            "success": race_saved.id
        })