
from django.urls import path
from billapp import views

urlpatterns = [
    path('',views.index, name="index"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
]