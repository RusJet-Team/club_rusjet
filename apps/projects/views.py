from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.projects.models import Project


class ProjectDetailView(DetailView):

    model = Project
    template_name = "projects/project_detail.html"


class ProjectsListView(ListView):

    model = Project
    template_name = "projects/project_list.html"
