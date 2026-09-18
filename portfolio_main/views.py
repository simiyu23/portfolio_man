from django.shortcuts import render
from ports.models import Port, Category
from assignments.models import About
from .forms import RegistartionForm
from django.contrib.auth.forms import AuthenticationFrom


def home(request):
    categories = Category.objects.all()
    featured_posts = Port.objects.filter(is_featured=True,)
    posts = Port.objects.filter(is_featured=False, status='published')

    # Fetch about us

    try:
        about = About.objects.all()
    execpt:
        about = None
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,

    }

    return render(request, 'home.html', context)

    def register(request)
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register .hmtl', context)

    def login(request):

            form.AuthenticationFrom()
            context = {
                 'form': form,
            }

        return render(request, 'login.html', context)
