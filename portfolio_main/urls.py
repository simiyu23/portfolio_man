from django.contrib import admin
from django.urls import path, include
from ports import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Homepage
    path("", views.home, name="home"),

    # Categories
    path("category/", include("ports.urls")),

    # Individual blog/portfolio post
    path("<slug:slug>/", views.ports, name="Ports"),

    # Search
    path("ports/search/", views.search, name="search"),
]


# Media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
