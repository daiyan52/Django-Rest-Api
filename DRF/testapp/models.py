from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=25)
    esal = models.FloatField()
    eaddress = models.CharField(max_length=100)


# (env) daiyanalam@Daiyans-MacBook-Air DRF % python3 manage.py shell
# Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from testapp.models import Employee
# >>> from testapp.serializers import EmployeeSerializer
# >>> emp = Employee.objects.get(id=1)
# >>> emp
# <Employee: Employee object (1)>
# >>> emp.ename
# 'Daiyan Alam'
# >>> emp.esal
# 890000.0
# >>> emp.eaddress
# 'Siwan, Bihar'
# >>> eserializers = EmployeeSerializer(emp)
# >>> eserializers.data
# {'ename': 'Daiyan Alam', 'esal': 890000.0, 'eaddress': 'Siwan, Bihar'}
# >>> 
    



# (env) daiyanalam@Daiyans-MacBook-Air DRF % python3 manage.py shell
# Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from testapp.models import Employee
# >>> from testapp.serializers import EmployeeSerializer
# >>> qs = Employee.objects.all()
# >>> eserializer = EmployeeSerializer(qs, many=True)
# >>> eserializer.data
# >>> from rest_framework.renderers import JSONRenderer
# >>> json_data = JSONRenderer().render(eserializer.data)
# >>> json_data