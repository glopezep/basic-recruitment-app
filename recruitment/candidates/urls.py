from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.new_view, name="new_candidate")
]
