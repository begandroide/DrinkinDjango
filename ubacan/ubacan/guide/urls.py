from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#     # ex: /polls/1/
#     path('<int:tramite_id>/', views.detail, name='detail'),

]