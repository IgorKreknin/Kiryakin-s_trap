from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', index),
    path('API/', include('API.urls')),
    path('authback/', include('authback.urls')),
    path('admin/', admin.site.urls),
]
