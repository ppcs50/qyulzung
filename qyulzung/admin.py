from django.contrib import admin

# Register your models here.
from .models import QZ, Topic

admin.site.register(QZ)
admin.site.register(Topic)