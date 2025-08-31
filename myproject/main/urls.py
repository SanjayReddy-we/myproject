from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                 # shows your index.html
    path("get-response/", views.get_response, name="get_response"),  # backend API
]
