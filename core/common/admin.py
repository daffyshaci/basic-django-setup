from django.contrib import admin
from .models import TestCommon, TestAfter


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_at', 'update_at')

class Test2Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_at', 'update_at')


admin.site.register(TestCommon, TestAdmin)
admin.site.register(TestAfter, Test2Admin)
