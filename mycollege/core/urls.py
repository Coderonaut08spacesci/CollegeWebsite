from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('principal-message/', views.principal_message, name='principal-message'),
    path('courses/', views.courses, name='courses'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('fees/', views.fees, name='fees'),
    path('admission/', views.admission, name='admission'),
]