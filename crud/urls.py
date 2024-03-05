from django.urls import path, re_path
from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.create_group, name='create_group'),
    path('groups/<int:id>/update', views.update_group, name='update_group'),
    path('groups/<int:id>/delete', views.delete_group, name='delete_group'),
    path('students/', views.create_student, name='create_student'),
    path('students/<int:id>/update', views.update_student, name='update_student'),
    path('students/<int:id>/delete', views.delete_student, name='delete_student'),
]