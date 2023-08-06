from django.urls import path
from meigen_app.views import (Login, add_user, MeigenAPI)

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_user/', views.add_user, name="add_user"),
    path('login/', Login.as_view()),
    path('data/', MeigenAPI.as_view()),
]
