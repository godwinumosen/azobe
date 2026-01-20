# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date


class CarouselMainPicture(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    img = models.ImageField(upload_to='carousel/')
    publish_date = models.DateTimeField (auto_now_add= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
       
    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
    
# The main model for Deus Magnus Model category
class AzobeojMainPost(models.Model):
    azobeoj_title = models.CharField(max_length=255, blank=True, null=True)
    azobeoj_description = models.TextField()
    azobeoj_description_2 = models.TextField()
    azobeoj_slug = models.SlugField (max_length=255,blank=True, null=True)
    azobeoj_magnus_img = models.ImageField(upload_to='images/')
    azobeoj_magnus_img_1 = models.ImageField(upload_to='images_1/')
    azobeoj_magnus_img_2 = models.ImageField(upload_to='images_2/')
    azobeoj_publish_date = models.DateTimeField (auto_now_add= True)
    azobeoj_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-azobeoj_publish_date']
    
    def __str__(self):
        return self.azobeoj_title + ' | ' + str(self.azobeoj_author)
    
    def get_absolute_url(self):
        return reverse('home')
    

# The Last Azobeoj Model category
class LastAzobeojMainPost(models.Model):
    last_title = models.CharField(max_length=255, blank=True, null=True)
    last_description = models.TextField()
    last_slug = models.SlugField (max_length=255,blank=True, null=True)
    last_magnus_img = models.ImageField(upload_to='last_images/')
    last_publish_date = models.DateTimeField (auto_now_add= True)
    last_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-last_publish_date']
    
    def __str__(self):
        return self.last_title + ' | ' + str(self.last_author)
    
    def get_absolute_url(self):
        return reverse('home')
    
#The Contactvideo on deusmagnus website
class Contactvideo(models.Model):
    contact_video = models.FileField(upload_to='contact_videos/') 
    
    
# The Azobeoj Projects Model category
class AzobeojProjectsMainPost(models.Model):
    projects_title = models.CharField(max_length=255, blank=True, null=True)
    projects_description = models.TextField()
    projects_slug = models.SlugField (max_length=255,blank=True, null=True)
    projects_magnus_img = models.ImageField(upload_to='project_images/')
    projects_publish_date = models.DateTimeField (auto_now_add= True)
    projects_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-projects_publish_date']
    
    def __str__(self):
        return self.projects_title + ' | ' + str(self.projects_author)
    
    def get_absolute_url(self):
        return reverse('home')
    


class TeamsMainPost(models.Model):
    team_title = models.CharField(max_length=255, blank=True, null=True)
    team_description = models.TextField()
    team_slug = models.SlugField (max_length=255,blank=True, null=True)
    team_magnus_img = models.ImageField(upload_to=' team_images/')
    team_publish_date = models.DateTimeField (auto_now_add= True)
    team_author = models.ForeignKey(User, on_delete=models.CASCADE)

       
    class Meta:
        ordering =['-team_publish_date']
    
    def __str__(self):
        return self.team_title + ' | ' + str(self.team_author)
    
    def get_absolute_url(self):
        return reverse('home')