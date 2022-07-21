from django.contrib import admin

from .models import Container, Temperature_Reading

admin.site.register(Container)
admin.site.register(Temperature_Reading)
