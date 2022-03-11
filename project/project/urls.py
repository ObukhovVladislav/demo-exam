from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('login/', include('authapp.urls', namespace='auth')),

    path('admin/', admin.site.urls),
]
