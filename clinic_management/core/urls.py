from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('signup/', views.signup, name='signup'),  # Sign-up page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'), 
    path('patients/', views.patients_list, name='patients_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<int:pk>/edit/', views.edit_patient, name='edit_patient'),
    path('patients/<int:pk>/delete/', views.delete_patient, name='delete_patient'),
    path('medicines/', views.medicines_list, name='medicines_list'),
    path('medicines/add/', views.add_medicine, name='add_medicine'),
    path('medicines/<int:pk>/edit/', views.edit_medicine, name='edit_medicine'),
    path('medicines/<int:pk>/delete/', views.delete_medicine, name='delete_medicine'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/<int:pk>/edit/', views.edit_doctor, name='edit_doctor'),
    path('doctors/<int:pk>/delete/', views.delete_doctor, name='delete_doctor'),
    path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/<int:pk>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:pk>/delete/', views.delete_appointment, name='delete_appointment'),
]
