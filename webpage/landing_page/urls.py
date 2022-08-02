import imp
from django.urls import path
from . import views

app_name = 'landing_page'

urlpatterns = [
    #homepage
    path('', views.home, name='home'),
    path('contact-us/', views.contact_us, name='contact_us')
]
