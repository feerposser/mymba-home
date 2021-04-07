from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.core.cache import cache

from .models import ModelTestimony, ModelFAQ as FAQ
from projects.models import ModelActivity as Activity, ModelContributor as Contributors, \
    ModelTypeActivity as TypeActivity
from .forms import FormContact
from utils.utils import get_total_impacted_animals


class ViewHome(View):
    template = "home/index.html"

    def get(self, request):
        impacted_cache_animals = cache.get_or_set("impacted_animals", get_total_impacted_animals())

        return render(request, self.template, {"testemonials": ModelTestimony.objects.all(),
                                               "types_activities": TypeActivity.objects.all().exclude(type="deleted"),
                                               "data_activities": Activity.objects.all()[:3],
                                               "contributors": Contributors.objects.count(),
                                               "impacted_animals": impacted_cache_animals,
                                               "questions": FAQ.objects.all()})

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
