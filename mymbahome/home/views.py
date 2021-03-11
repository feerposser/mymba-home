from django.shortcuts import render
from django.views import View


class ViewHome(View):
    template = "home/index.html"

    def get(self, request):
        return render(request, self.template)
