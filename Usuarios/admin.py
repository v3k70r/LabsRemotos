from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'es_mentor', 'es_admin', )


admin.site.register(Usuario, UserAdmin)
admin.site.register(Entrada)
admin.site.register(Banner)
