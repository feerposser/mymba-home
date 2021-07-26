from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.core.cache import cache

from .models import ModelTestimony, ModelFAQ as FAQ, ModelNewsletterAssign as Newsletter
from projects.models import ModelActivity as Activity, ModelContributor as Contributors, \
    ModelTypeActivity as TypeActivity
from .forms import FormContact, FormNewsletterAssign
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


class ViewNewsletterAssign(View):
    """
    Create an object in NewsletterAssign. The basic to start. In the future a microsservice for newsletter will be
    necessary to handle all the newsletter stuff.
    """
    def post(self, request):
        try:
            newsletter_assign = FormNewsletterAssign(request.POST)
            if newsletter_assign.is_valid():
                newsletter_assign.save()
                messages.add_message(request, messages.SUCCESS, "A partir de agora você faz parte do clube! (:")
            else:
                messages.add_message(request, messages.ERROR,
                                     "Houve algum problema ao cadastrar seu email :(\n erro: {}".format(
                                         newsletter_assign.errors.items()))
                print(newsletter_assign.errors.items())
        except Exception as e:
            print("======", e)
        return HttpResponseRedirect("/")


def open_source(request):
    return render(request, "home/open-source.html")

def ecossystem(request):
    return render(request, "home/ecosystem.html")

def smart_collar(request):
    return render(request, "home/beallar.html")

def smart_feeder(request):
    return render(request, "home/smart-feeder.html")

def edu(request):
    return render(request, "home/mymba-edu.html")

def temp_home(request):
    return render(request, "home/temp-home.html")

def vet(request):
    return render(request, "home/vet.html")

def partners(request):
    return render(request, "home/partners.html")

def about(request):
    return render(request, "home/about.html")
