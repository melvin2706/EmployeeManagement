from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    
    # department
    path('department_index/',views.department_index),
    path('departments/',views.all_departments, name='departments'),
    path('department/<int:pk>',views.department, name='depatment'),
    path('add_department/',views.add_department, name='add_department'),
    path('update_department/<int:pk>',views.update_department, name='update_depatment'),
    path('delete_department/<int:pk>',views.delete_department, name='del_department'),

    # service
    path('service_index/',views.service_index),
    path('services/',views.all_services, name='services'),
    path('service/<int:pk>',views.service, name='service'),
    path('add_service/',views.add_service, name='add_service'),
    path('add_service_department/<int:pk>',views.add_service_department, name='add_service_department'),
    path('update_service/<int:pk>',views.update_service, name='update_service'),
    path('delete_service/<int:pk>',views.delete_service, name='del_service'),
    path('delete_department_service/<int:dpk>/<int:spk>',views.delete_department_service, name='del_department_service'),

    # post
    path('post_index/',views.post_index),
    path('posts/',views.all_posts, name='posts'),
    path('post/<int:pk>',views.post, name='post'),
    path('add_post/',views.add_post, name='add_post'),
    path('update_post/<int:pk>',views.update_post, name='update_post'),
    path('delete_post/<int:pk>',views.delete_post, name='del_post'),

    # meeting
    path('meeting_index/',views.meeting_index),
    path('meetings/',views.all_meetings, name='meetings'),
    path('meeting/<int:pk>',views.meeting, name='meeting'),
    path('add_meeting/',views.add_meeting, name='add_meeting'),
    path('update_meeting/<int:pk>',views.update_meeting, name='update_meeting'),
    path('delete_meeting/<int:pk>',views.delete_meeting, name='del_meeting'),

    # project
    path('project_index/',views.project_index),
    path('projects/',views.all_projects, name='projects'),
    path('project/<int:pk>',views.project, name='project'),
    path('add_project/',views.add_project, name='add_project'),
    path('update_project/<int:pk>',views.update_project, name='update_project'),
    path('delete_project/<int:pk>',views.delete_project, name='del_project'),


    # task
    path('task_index/',views.task_index),
    path('tasks/',views.all_tasks, name='services'),
    path('task/<int:pk>',views.task, name='service'),
    path('add_task/',views.add_task, name='add_task'),
    path('add_project_task/<int:pk>',views.add_task_to_project, name='add_project_task'),
    path('update_task/<int:pk>',views.update_task, name='update_task'),
    path('delete_task/<int:pk>',views.delete_task, name='del_task'),
    path('delete_task_project/<int:ppk>/<int:tpk>',views.delete_task_from_project, name='del_project_task'),

]