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

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name','profile_picture', 'title','bio', 'email', 'phone', 'location', 'dob', 'degree')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title','issuer','issue_date','certificate_url')