# app/urls.py

from django.urls import path, include

app_name = 'app'

urlpatterns = [
    path('api/v1/', include('xldashboard.routes.api')),
]
