from django.contrib import admin
from . models import Food, Classroom, School, Classroom_Food
# Register your models here.
admin.site.register(Food)
admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Classroom_Food)