from django.contrib import admin
from core.models import Categories, Sentences

admin.site.register((
    Categories, Sentences
))