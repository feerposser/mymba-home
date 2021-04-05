from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import ModelActivity as Activities, ModelTypeActivity as TypeActivity


class ViewActivities(View):
    template = "home/list-main-content.html"

    def get(self, request):
        return render(request, self.template, {
            "title": "ATIVIDADES",
            "types_activities": TypeActivity.objects.all().exclude(type="deleted"),
            "data": Activities.objects.all()})


class ViewActivity(View):
    template = "home/activity-detail.html"

    def get(self, request, id, slug_name):

        activity = get_object_or_404(Activities, id=id)

        return render(request, self.template, {
            "activity": activity
        })