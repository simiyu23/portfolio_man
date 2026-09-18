from django.shortcuts import render

from django.shortcuts import render
from .models import About


def about(request):
    about = About.objects.first()

    context = {
        'about': about,
    }

    return render(request, 'about.html', context)

    def register(request):
        return render(request, register.hmtl)
