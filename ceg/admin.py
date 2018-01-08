from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ceg.models import Project, UserProject, UserProfile, Protocol, Baud_Rate, Data_Flows

# Register your models here.
# Importing the models is necessary in order for django to recognize the model
# These models can be accessed in the django admin site
# Make sure it follows the below pattern with the model name in parenthesis
admin .site.register(Project)
admin.site.register(UserProfile)
admin.site.register(UserProject)

admin.site.register(Protocol)
admin.site.register(Baud_Rate)
admin.site.register(Data_Flows)
