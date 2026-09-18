
from django.contrib import admin
from django.urls import path, include
from ports import views

urlpatterns = [

    path("admin/", admin.site.urls),

    # Home page
    path("", views.home, name="home"),

    # Register
    path("register/", views.register, name="register"),

    # Login
    path("login/", views.user_login, name="login"),

    # Search
    path("search/", views.search, name="search"),

    # Categories
    path("category/", include("ports.urls")),

    # Individual blog post
    path("<slug:slug>/", views.ports, name="Ports"),

    # logout
    path("logout/", views.logout_view, name="logout"),
]
