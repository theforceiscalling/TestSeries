from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='taketest_index'),
]