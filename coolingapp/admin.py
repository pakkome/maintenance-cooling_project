from django.contrib import admin
from coolingapp.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(Teacher)

admin.site.register(CustomUser, UserAdmin)