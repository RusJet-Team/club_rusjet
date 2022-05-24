from django.urls import path

from apps.projects.views import ProjectDetailView, ProjectsListView

urlpatterns = [
    path("projects/", ProjectsListView.as_view(), name="projects_list"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="projects_detail"),
]
