from django.urls import path
from . import views
urlpatterns = [
    # ... other URL patterns ...
    path('url/task/', views.task_page, name='task_page'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Include your app's URLs here
]
