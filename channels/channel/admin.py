from django.contrib import admin

from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
admin.site.register(Channel, ChannelAdmin)
