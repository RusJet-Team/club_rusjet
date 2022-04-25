# from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "develop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class PortfolioDetailsView(TemplateView):

    template_name = "portfolio-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


# def index(request):
#     # post_list = Post.objects.all()
#     # paginator = Paginator(post_list, 10)
#     # page_number = request.GET.get("page")
#     # page = paginator.get_page(page_number)
#     return render(request, "index.html")
