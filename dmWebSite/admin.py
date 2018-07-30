from django.contrib import admin
from .models import dmWebsiteUser
from .models import dmWebsiteUserOnlyEmails
from .models import dmWebsiteContactUs

# Register your models here.
class dmWebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'user_phone')
    search_fields = ('user_name', 'user_email', 'user_phone')
    list_filter = ('user_name',)
admin.site.register(dmWebsiteUser, dmWebsiteUserAdmin)

class dmWebsiteUserOnlyEmailsAdmin(admin.ModelAdmin):
    list_display = ('user_email',)
    search_fields = ('user_email',)
    list_filter = ('user_email',)
admin.site.register(dmWebsiteUserOnlyEmails, dmWebsiteUserOnlyEmailsAdmin)

class dmWebsiteContactUsAdmin(admin.ModelAdmin):
    list_display = ('user_email','user_first_name','user_last_name', 'user_message')
    search_fields = ('user_email',)
    list_filter = ('user_email',)
admin.site.register(dmWebsiteContactUs, dmWebsiteContactUsAdmin)