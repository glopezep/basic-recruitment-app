from django.urls import path

from . import views

urlpatterns = [
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='home/',
        view=views.home_view,
        name='home'
    ),
    path(
        route='reclutar/<int:id>/',
        view=views.reclutar_view,
        name='reclutar'
    ),
    path('report/', views.Pdf.as_view(), name="report")

]
