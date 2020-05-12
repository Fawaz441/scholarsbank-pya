from django.contrib import admin
from .models import School,Coursefiles,Course,Material,Products

admin.site.register(Products)
admin.site.register(Material)
admin.site.register(School)
admin.site.register(Course)
admin.site.register(Coursefiles)

