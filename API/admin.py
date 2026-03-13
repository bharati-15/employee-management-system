from django.contrib import admin
from .models import EmployeeDetails, Department, Skills, Training, EmployeeSkills
# Register your models here.
from .models import *

class employee_details_Admin(admin.ModelAdmin):
    list_display=('first_name','last_name','id','employment_id')
    list_display_links=('first_name','id')
    list_editable=('last_name','last_name')

class department_admin(admin.ModelAdmin):
    list_display=('name_of_department','id','department_code','created_at')
    list_editable=('name_of_department',)
    list_display_links=('id',)

admin.site.register(EmployeeDetails, employee_details_Admin)

admin.site.register(Department,department_admin)

admin.site.register(Skills)
admin.site.register(Training)
admin.site.register(EmployeeSkills)