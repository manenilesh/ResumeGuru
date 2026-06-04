from django.urls import path
from . import views


urlpatterns = [
    path('check/', views.ats_score_view, name='ats_score'),
]