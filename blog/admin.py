from django.contrib import admin
from . import models
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

@csrf_protect
@admin.site.register(models.Category)

@csrf_protect

admin.site.register(models.Carousel)