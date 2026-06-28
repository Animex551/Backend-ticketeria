from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Corrige esta línea: debe ser admin.site.urls
    path('admin/', admin.site.urls), 
    path('api/', include('mi_api.urls')),
]