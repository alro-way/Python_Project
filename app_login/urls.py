from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('create_user', views.create_user),
    path('login_user', views.login_user),

    # path('create_instructor', views.create_instructor),
    # path('login_user', views.login_user),
]