from django.contrib import admin
from .models import dmWebsiteUser

# Register your models here.
class dmWebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'user_phone')
admin.site.register(dmWebsiteUser, dmWebsiteUserAdmin)