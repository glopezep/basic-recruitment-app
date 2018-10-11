from django.urls import path

from . import views

urlpatterns = [
    path(
        route='new/',
        view=views.new_view,
        name='new_candidate'
    ),
    path(
        route='new_experience/',
        view=views.new_experience_view,
        name='new_experience',
    ),
     path(
        route='detail/<int:cedula>',
        view=views.detail_view,
        name='detail',
    ),
    path(
        route='login/',
        view=views.login_view,
        name='login',
    )
]
