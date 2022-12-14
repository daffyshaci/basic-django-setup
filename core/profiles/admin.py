from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pkid", "id", "user", "gender")
    list_display_links =  ("id", "user")

admin.site.register(Profile, ProfileAdmin)
