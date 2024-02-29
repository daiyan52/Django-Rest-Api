from django.contrib import admin
from testapp.models import Student
# Register your models here.

class  StdentAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','address')

admin.site.register(Student,StdentAdmin)