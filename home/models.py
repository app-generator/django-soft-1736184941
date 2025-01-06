# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Books(models.Model):

    #__Books_FIELDS__
    book_id = models.TextField(max_length=255, null=True, blank=True)
    book_name = models.TextField(max_length=255, null=True, blank=True)
    book_publish_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Books_FIELDS__END

    class Meta:
        verbose_name        = _("Books")
        verbose_name_plural = _("Books")


class Updates(models.Model):

    #__Updates_FIELDS__
    book_id = models.ForeignKey(books, on_delete=models.CASCADE)

    #__Updates_FIELDS__END

    class Meta:
        verbose_name        = _("Updates")
        verbose_name_plural = _("Updates")



#__MODELS__END
