from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.

@admin.register(ResumeUpload)
class ResumeUploadAdmin(admin.ModelAdmin):
    list_display = ['resume']



class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    technologies = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = '__all__'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = (
        'title',
        'description',
        'technologies',
        'github_link',
        'live_demo_link',
        'demo_video',
        'created_from',
        'created_to',
    )
