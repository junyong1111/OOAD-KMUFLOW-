from django.urls import path

from . import views

app_name = 'kmuflow'
urlpatterns = [
	path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('search', views.search, name='search'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]