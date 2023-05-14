from django.urls import path
from crud import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.view_courses, name='courses'),
    path('course/detail/course_id/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/add/', views.add_new_course, name='add-course'),
    path('course/edit/<int:pk>/', views.edit_course, name='edit-course'),


    path('student/add/', views.add_student, name='add-student'),
    path('students/', views.view_students, name='view-students'),
    path('student/edit/<int:pk>/', views.edit_student, name='edit-student'),
    path('student/delete/<int:pk>/', views.delete_student, name='delete-student'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]