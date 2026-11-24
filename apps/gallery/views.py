from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "gallery/pages/index.html"