from django.urls import path

from project_name.apps.users.views import ping

urlpatterns = [
    path('', ping.as_view()),
]