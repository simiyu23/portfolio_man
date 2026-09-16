from django.contrib import admin
from .models import Category, Port


class PortAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'author', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)


admin.site.register(Category)
admin.site.register(Port, PortAdmin)
