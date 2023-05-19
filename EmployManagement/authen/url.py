from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.signIn, name='login'),
    path('logout/', views.log_out, name='logout'),
    
    # project
    path('user_index/',views.user_index),
    path('users/',views.all_users, name='users'),
    path('user/<int:pk>',views.user, name='user'),
    path('add_user/',views.add_user, name='add_user'),
    path('add_user_service/<int:pk>',views.add_user_service, name='add_user_service'),
    path('update_user/<int:pk>',views.update_user, name='update_user'),
    path('delete_user/<int:pk>',views.delete_user, name='del_user'),
]