from django.contrib import admin
from django.db import models
from usermanagementsystem.models import Adduser

# Register your models here.
 
# admin.site.register(Adduser)
class AdduserAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','Age']
admin.site.register(Adduser)
