from django.shortcuts import render
from django.views import View

from .models import ModelTestimony
from projects.models import ModelProject as Projects, ModelAction as Actions, ModelContributor as Contributors


class ViewHome(View):
    template = "home/index.html"

    def get(self, request):

        return render(request, self.template, {"testemonials": ModelTestimony.objects.all(),
                                               "projects": Projects.objects.count(),
                                               "contributors": Contributors.objects.count(),
                                               "actions": Actions.objects.count()})

