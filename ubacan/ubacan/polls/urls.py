from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /courses/
    path('courses/', views.courses, name='courses'),

]