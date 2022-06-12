from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.projects.models import Project, ProjectImage


class ProjectDetailView(DetailView):

    model = Project
    template_name = "projects/project_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["project_images"] = ProjectImage.objects.filter(project=self.object)
        return self.render_to_response(context)


class ProjectsListView(ListView):

    model = Project
    template_name = "projects/project_list.html"
