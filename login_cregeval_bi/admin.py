from django.contrib import admin
from login_cregeval_bi.models import CregevalUSer


# Register your models here.

class CregevalUsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(CregevalUSer, CregevalUsersAdmin)
