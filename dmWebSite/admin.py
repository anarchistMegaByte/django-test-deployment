from django.contrib import admin
from .models import dmWebsiteUser
from .models import dmWebsiteUserOnlyEmails
from .models import dmWebsiteContactUs,dmWebsiteSubmitProjectDetails

# Register your models here.
class dmWebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'user_phone','sts')
    search_fields = ('user_name', 'user_email', 'user_phone', 'sts')
    list_filter = ('user_name','sts')
admin.site.register(dmWebsiteUser, dmWebsiteUserAdmin)

class dmWebsiteUserOnlyEmailsAdmin(admin.ModelAdmin):
    list_display = ('user_email','sts')
    search_fields = ('user_email','sts')
    list_filter = ('user_email','sts')
admin.site.register(dmWebsiteUserOnlyEmails, dmWebsiteUserOnlyEmailsAdmin)

class dmWebsiteContactUsAdmin(admin.ModelAdmin):
    list_display = ('user_email','user_first_name','user_last_name', 'user_message','sts')
    search_fields = ('user_email','sts')
    list_filter = ('user_email','sts')
admin.site.register(dmWebsiteContactUs, dmWebsiteContactUsAdmin)

class dmWebsiteSubmitProjectDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_phone_number','user_email', 'user_institution','user_domain','sts','user_project_title','user_project_description')
    search_fields = ('user_name','user_phone_number','user_email', 'user_institution','user_domain','sts','user_project_title','user_project_description')
    list_filter = ('user_name','user_phone_number','user_email', 'user_institution','user_domain','sts')
admin.site.register(dmWebsiteSubmitProjectDetails, dmWebsiteSubmitProjectDetailsAdmin)