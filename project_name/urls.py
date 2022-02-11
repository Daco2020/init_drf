from django.contrib import admin
from django.urls    import path, include


urlpatterns = [
    path('admin', admin.site.urls),
    path('users', include('project_name.apps.users.urls')),
]