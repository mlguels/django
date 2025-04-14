from django.contrib import admin
from django.urls import path
from projectname import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/files/', views.files, name='files'),
    path('api/files/<int:file_id>/', views.file, name='file')
]

urlpatterns = format_suffix_patterns(urlpatterns)
