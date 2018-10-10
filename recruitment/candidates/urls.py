from django.urls import path

from . import views

urlpatterns = [
    path(
        route='new/',
        view=views.new_view,
        name='new_candidate'
    )
]
