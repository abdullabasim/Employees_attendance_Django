from . import views
from django.urls import path ,include

urlpatterns = [

    path("attendance/", views.getEmployeeAttendance,name='attendance'),


]