from django.urls import path
from. import views

urlpatterns = [
    path('student/',views.studentView),
    path('studentJson/',views.studentJsonView),
    path('studentJson2/',views.studentJsonView2),
]
