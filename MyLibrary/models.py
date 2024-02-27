from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

class Language(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)

class User(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('librarian', 'Librarian'),
        ('admin', 'Admin'),
    )
    username = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)


