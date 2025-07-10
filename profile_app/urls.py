from django.urls import path
from . import views

urlpatterns = [
    path('resume/',views.resume_view,name='resume'),
    path('project/',views.project_view,name='project'),
    path('about/', views.about_view, name='about'),
]
