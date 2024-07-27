from django.contrib import admin
from .models import *
from django.utils.html import format_html
# customize the admin page

class TeamAdmin(admin.ModelAdmin):
    
    def thumbnail(self,object):
        return format_html('<img src = "{}" width = "40" style = "border-radius : 50%" />'.format(object.avatar.url))
    
    thumbnail.short_description = 'avatar'
    
    # display the data in table
    list_display = ('id','thumbnail','first_name','last_name','designation','created_date')
    
    # to open the data by click on first_name
    list_display_links = ('id','first_name',)
    
    # to search with specific paramter like name,designation in django admin db
    search_fields = ('first_name','id','designation')
    
    # filter the data using particular designation
    list_filter = ('designation',)


# Register your models here.
admin.site.register(Team,TeamAdmin)

