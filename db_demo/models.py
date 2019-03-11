from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User

# Your models go here!


class Profile(models.Model):
    avatar = models.CharField(max_length=45)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Roles(models.Model):
    title = models.CharField(max_length=45)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Categories(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.title


class Contributors(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Permissions(models.Model):
    title = models.CharField(max_length=45)

    def __str__(self):
        return self.title


class Tags(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Pages(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_published = models.SmallIntegerField()
    is_flagged = models.SmallIntegerField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
