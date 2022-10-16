from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import misaka

from django.contrib.auth import get_user_model

User = get_user_model()

from django import template

register = template.Library()


# Create your models here.


class Group(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    DoesNotExist = None
    objects = models.Manager
    groups = models.ForeignKey(Group, related_name="membership", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("groups", "user")



































# Many-to-one fields:
# This is used when one record of a model A is related to multiple records of another model B. For example – a model Song has many-to-one relationship with a model Album, i.e. an album can have many songs, but one song cannot be part of multiple albums. Many-to-one relations are defined using ForeignKey field of django.db.models.

# Many-to-many fields:
# This is used when one record of a model A is related to multiple records of another model B and vice versa. For example – a model Book has many-to-many relationship with a model Author, i.e. an book can be written by multiple authors and an author can write multiple books. Many-to-many relations are defined using ManyToManyField field of django.db.models.

# One-to-one fields:
# This is used when one record of a model A is related to exactly one record of another model B. This field can be useful as a primary key of an object if that object extends another object in some way. For example – a model Car has one-to-one relationship with a model Vehicle, i.e. a car is a vehicle. One-to-one relations are defined using OneToOneField field of django.db.models.

