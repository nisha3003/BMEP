from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('volunteers.urls')),
    path('admin/', admin.site.urls),
    path('volunteers/', include('volunteers.urls')),
]
