from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html", context=None)

class Home404View(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "404.html", context=None)


