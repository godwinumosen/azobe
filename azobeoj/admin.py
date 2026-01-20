from django.contrib import admin
# Register your models here.
from . import models

from .models import CarouselMainPicture,AzobeojMainPost,LastAzobeojMainPost,Contactvideo
from .models import AzobeojProjectsMainPost,TeamsMainPost

#The CarouselMainPicture post model admin
class MainPostModelAdmin (admin.ModelAdmin):
    list_display = ['author','title','publish_date']
admin.site.register(CarouselMainPicture, MainPostModelAdmin)

class AzobeojMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'azobeoj_slug': ('azobeoj_title',)}
    list_display = ['azobeoj_title','azobeoj_description','azobeoj_author']
admin.site.register(AzobeojMainPost, AzobeojMainPostModelAdmin)

class LastAzobeojModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'last_slug': ('last_title',)}
    list_display = ['last_title','last_description','last_author']
admin.site.register(LastAzobeojMainPost, LastAzobeojModelAdmin)

class ContactvideoModelAdmin (admin.ModelAdmin):
    list_display = ['contact_video']
admin.site.register(Contactvideo, ContactvideoModelAdmin)

class AzobeojProjectsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'projects_slug': ('projects_title',)}
    list_display = ['projects_title','projects_description','projects_author']
admin.site.register(AzobeojProjectsMainPost, AzobeojProjectsModelAdmin)

class TeamsMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'team_slug': ('team_title',)}
    list_display = ['team_title','team_description','team_author']
admin.site.register(TeamsMainPost, TeamsMainPostModelAdmin)