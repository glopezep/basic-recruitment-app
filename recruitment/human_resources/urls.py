from django.urls import path

from . import views

urlpatterns = [
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='home/',
        view=views.home_view,
        name='home'
    ),
]
