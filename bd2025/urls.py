from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("inscription/", views.inscription, name="contact"),
    path("affectation/", views.affectation, name="affectation"),
    path("success/", lambda request: render(request, "success.html"), name="success")
]
