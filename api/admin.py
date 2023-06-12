from django.contrib import admin
from .models import MyModel,Student,Company

# Register your models here.
admin.site.register(MyModel)
admin.site.register(Student)
admin.site.register(Company)