from django.contrib import admin
from django.urls import path, include
#from rest_framework import routers


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
