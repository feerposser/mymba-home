from django.shortcuts import render
from django.views import View

from .models import ModelTestimony


class ViewHome(View):
    template = "home/index.html"

    def get(self, request):

        return render(request, self.template, {"testemonials": ModelTestimony.objects.all()})
