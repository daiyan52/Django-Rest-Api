from django.urls import path
from testapp import views

urlpatterns = [
    path('student/',views.studentView),
    path('studentJson/',views.studentJsonView),
    path('studentJson2/',views.studentJsonView2),
    path('apijsoncbv/',views.jsonCBV.as_view()),
    path('apijsoncbv1/',views.jsonCBV1.as_view()),

]