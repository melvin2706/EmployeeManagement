from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(Service)
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Meeting)