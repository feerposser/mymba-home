from django.shortcuts import render
from django.views import View

from .models import ModelActivity as Activities, ModelTypeActivity as TypeActivity


class ViewActivities(View):
    template = "home/list-main-content.html"

    def get(self, request):
        return render(request, self.template, {
            "title": "ATIVIDADES",
            "types_activities": TypeActivity.objects.all().exclude(type="deleted"),
            "data": Activities.objects.all()})
