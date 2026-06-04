from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_resume_view, name='create_resume'),
    path('library/', views.my_library_view, name='my_library'),
    path('templates/', views.resume_templates_view, name='resume_templates'),
    path('samples/', views.resume_samples_view, name='resume_samples'),
    path('view/<int:resume_id>/', views.view_resume_view, name='view_resume'),

    path('download/<int:resume_id>/', views.download_resume_pdf, name='download_resume_pdf'),
]