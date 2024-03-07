from django.urls import path
from testapp.views import EmployeeView
urlpatterns = [
    path('api/<int:id>/',EmployeeView.as_view())
]
