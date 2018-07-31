from django.db import models
from django.utils.timezone import now

# Create your models here.
class dmWebsiteUser(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=10)
    sts = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_name

class dmWebsiteUserOnlyEmails(models.Model):
    user_email = models.CharField(max_length=100)
    sts = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_name

class dmWebsiteContactUs(models.Model):
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_message = models.CharField(max_length=600)
    sts = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_email

class dmWebsiteSubmitProjectDetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone_number = models.CharField(max_length=10)
    user_email = models.CharField(max_length=50)
    user_institution = models.CharField(max_length=100)
    user_domain = models.CharField(max_length=200)
    user_project_title = models.CharField(max_length=200)
    user_project_description = models.CharField(max_length=600)
    sts = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_name
