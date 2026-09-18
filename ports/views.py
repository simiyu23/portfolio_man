from .models import Port, Category
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
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
    # Find the category
    category = Category.objects.filter(id=category_id).first()

    # If category does not exist, return to home
    if category is None:
        return redirect("home")

    # Get all categories
    categories = Category.objects.all()

    # Get published posts in this category
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
    return render(request, "ports.html")


def search(request):
    # Get keyword from URL
    keyword = request.GET.get("keyword", "")

    # Search published posts
    posts = Port.objects.filter(
        title__icontains=keyword,
        status="published"
    )

    context = {
        "posts": posts,
        "keyword": keyword,
    }

    return render(request, "search.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # Send user to login page
            return redirect("login")

    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }

    return render(request, "register.html", context)


def user_login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check username and password
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Django's real login function
            auth_login(request, user)

            # Send user to home page
            return redirect("home")

        # Wrong username/password
        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    # When opening /login/ with GET
    return render(request, "login.html")


def logout_view(request):
    # Log the user out
    auth_logout(request)

    # Send the user back to the home page
    return redirect("home")
