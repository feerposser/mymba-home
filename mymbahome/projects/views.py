from django.shortcuts import render
from django.views import View

from .models import ModelActivity as Activities


class ViewActivities(View):
    template = "home/list-main-content.html"

    def get(self, request):
        return render(request, self.template, {
            "title": "ATIVIDADES",
            "data_activities": Activities.objects.all()})
