from django.contrib import admin

# Register your models here.
from .models import HeroClass, Profession, Race, Raid

admin.site.register(Profession)
admin.site.register(Raid)
admin.site.register(HeroClass)
admin.site.register(Race)
