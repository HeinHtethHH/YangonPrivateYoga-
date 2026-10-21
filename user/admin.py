from django.contrib import admin
from .models import CustomUser,UserInap,Instructor

admin.site.register(CustomUser)
admin.site.register(UserInap)
admin.site.register(Instructor)
# Register your models here.
