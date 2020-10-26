from django.contrib import admin
from App1.models import Theatre_Movie,TV_Movies
# Register your models here.
class TheatreAdmin(admin.ModelAdmin):
    list_display=['Title','Release_year','Genres','Description','Theatre']


class TVAdmin(admin.ModelAdmin):
    list_display=['Title','Release_year','Genres','Description','Channel']
admin.site.register(Theatre_Movie,TheatreAdmin)
admin.site.register(TV_Movies,TVAdmin)