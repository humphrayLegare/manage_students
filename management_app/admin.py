from django.contrib import admin

from .models import School, Student, Program, Field, Sex


# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Program)
admin.site.register(Field)
admin.site.register(Sex)
