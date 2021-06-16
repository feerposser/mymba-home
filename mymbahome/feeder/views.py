from django.shortcuts import render


def map(request):
    return render(request, "feeder/feeders.html")
