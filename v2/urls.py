from django.urls import path
from django.urls.conf import path
from .views import *
app_name = "v2"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('professions/', ProfessionsView.as_view()),
    path('professions/<int:pk>/', ProfessionView.as_view()),
    path('raids/', RaidsView.as_view()),
    path('raids/<int:pk>/', RaidView.as_view()),
    path('classes/', HeroClassesView.as_view()),
    path('classes/<int:pk>/', HeroClassView.as_view()),
    path('racies/', RaciesView.as_view()),
    path('racies/<int:pk>/', RaceView.as_view()),
]
