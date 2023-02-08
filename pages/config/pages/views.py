from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'

    # Create your views here.
class BasePageView(TemplateView):  # new
    template_name = 'base.html'