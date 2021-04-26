from django.urls import path, include
from . import views

app_name = 'demo_app'


urlpatterns = [
    path('', views.basic_content, name='home'),
    path('table/', views.basic_table, name='table'),
    path('form/', views.basic_form, name='form'),
    path('bootstrap_form/', views.bootstrap_form, name='form'),
]
