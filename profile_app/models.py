from django.db import models
import os
from ckeditor.fields import RichTextField
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.

class ResumeUpload(models.Model):
    resume = models.FileField(upload_to='resume/')

    def save(self,*args, **kwargs):
        for obj in ResumeUpload.objects.exclude(id=self.id):
            if obj.resume and os.path.isfile(obj.resume.path):
                os.remove(obj.resume.path)
            obj.delete()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.resume.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    technologies = RichTextField()
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    demo_video = models.FileField(upload_to='portfolio_videos/', blank=True, null=True)
    created_from = models.DateField()
    created_to = models.DateField()

    def __str__(self):
        return self.title


@receiver(post_delete,sender=Project)
def delete_demo_video_file(sender,instance,**kwargs):
    if instance.demo_video and os.path.isfile(instance.demo_video.path):
        os.remove(instance.demo_video.path)
