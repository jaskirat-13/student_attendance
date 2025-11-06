from django.contrib import admin
from django.urls import path, include
from attendance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('accounts/', include('attendance.urls')),
]
