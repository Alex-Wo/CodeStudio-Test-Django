from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('success/', views.feedback_success_view, name='feedback_success'),
    path('error/', views.feedback_error_view, name='feedback_error'),
]
