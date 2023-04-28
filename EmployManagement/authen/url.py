from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.signIn, name='login'),
    path('logout/', views.log_out, name='logout')
]