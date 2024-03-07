from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','eno','ename','esal','eaddress')
admin.site.register(Employee, EmployeeAdmin)