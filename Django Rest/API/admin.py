from django.contrib import admin

# Register your models here.
from .models import Category, Character

admin.site.register(Character)
admin.site.register(Category)