from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path('certificates',views.certificate,name='certificates'),
     path('contact',views.contact,name='contact'),
     path('projects',views.projects,name='projects'),
     path('about',views.about,name='about')
]