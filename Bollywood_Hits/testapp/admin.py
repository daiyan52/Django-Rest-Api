from django.contrib import admin
from testapp.models import Actor,Movie
# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname','age']
admin.site.register(Actor,ActorAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','hits_movie','actor','realsed_date','box_office_collection']
admin.site.register(Movie,MovieAdmin)