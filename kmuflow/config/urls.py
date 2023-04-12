from django.contrib import admin
from django.urls import path, include
from kmuflow import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kmuflow.urls')),
	path('kmuflow/', include('kmuflow.urls')),
    # path('kmuflow/', include('kmuflow.urls')),
]