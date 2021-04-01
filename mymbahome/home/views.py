from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import messages

from .models import ModelTestimony
from projects.models import ModelActivity as Activity, ModelContributor as Contributors
from .forms import FormContact


class ViewHome(View):
    template = "home/index.html"

    def get(self, request):
        return render(request, self.template, {"testemonials": ModelTestimony.objects.all(),
                                               "data_activities": Activity.objects.all()[:3],
                                               "contributors": Contributors.objects.count()})

    @staticmethod
    def post(request):
        contact = FormContact(request.POST)
        if contact.is_valid():
            contact.save()
            messages.add_message(request, messages.SUCCESS, "Recebemos sua mensagem (:")
        else:
            messages.add_message(request, messages.ERROR, "Houve um problema ao enviar a mensagem ): \n" +
                                 contact.errors)

        return HttpResponseRedirect("/")
