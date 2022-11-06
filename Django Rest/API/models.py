from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    content  = models.TextField(blank = True)
    category = models.ForeignKey("Category", on_delete = models.SET_NULL, null = True)


    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title