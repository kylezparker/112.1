from django.views.generic import TemplateView
# from .views import HomePageView, AboutPageView
# from django.urls import path


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name= "about.html"