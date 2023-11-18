from django.urls import path
from . import views

urlpatterns =[

  path( "", views.hello),
  path( "test/", views.test),
  path( "reg/", views.reg),
]


