
from django.contrib import admin

from django.urls import path ,include
from rest_framework_simplejwt.views import TokenVerifyView,TokenObtainPairView
urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/v1/', include('attendanceApp.urls')),
    path('api/v1/login/',TokenObtainPairView.as_view() ),
    path('api/v1/token/verify/',TokenVerifyView.as_view() ),
]
