from django.apps import apps

from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin


from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'email']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    
@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['date', 'status']
    search_fields = ['date', 'status']
    
class YourModelResource(ModelResource):
    class Meta:
        model = YourModel

class YourModelAdmin(ImportExportModelAdmin):
    resource_class = YourModelResource

admin.site.register(YourModel)
admin.site.register(Message)
admin.site.register(Email)
admin.site.register(Agenda)
admin.site.register(Chat)
admin.site.register(SupportQuestion)

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
    
    
