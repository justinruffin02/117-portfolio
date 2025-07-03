from django.urls import path
from .views import project_list

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [path("projects", project_list, name="projects-list" )]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
