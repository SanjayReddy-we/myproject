from django.contrib import admin
from django.urls import path, include  # de allows app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),      #  connects your main app
]
