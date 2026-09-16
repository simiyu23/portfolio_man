from .models import Port, Category
from django.shortcuts import render, redirect


def home(request):
    # Get all published posts
    posts = Port.objects.filter(status="published")

    # Get all categories
    categories = Category.objects.all()

    context = {
        "posts": posts,
        "categories": categories,
    }

    return render(request, "home.html", context)


def posts_by_category(request, category_id):

    # Try to find the category
    category = Category.objects.filter(id=category_id).first()

    # If the category does not exist,
    # send the user back to the homepage
    if category is None:
        return redirect("home")

    # Get all categories for the navigation/menu
    categories = Category.objects.all()

    # Get published posts belonging to this category
    posts = Port.objects.filter(
        status="published",
        category=category
    )

    context = {
        "posts": posts,
        "categories": categories,
        "category": category,
    }

    return render(request, "posts_by_category.html", context)


def ports(request, slug):
    return render(request, 'ports.html')


def search(request):
    keyworld = request.GET.get('keyworld')
    ports = Port.objects.filter(title__icontains=keyword, status='published')
    print(ports)
    context = {
        'ports': 'ports',
    }
    return render(request, 'search.html')
