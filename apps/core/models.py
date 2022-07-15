from django.db import models
# from django.contrib.auth import get_user_model


class PageSetting(models.Model):

    redirect_url = models.URLField(null=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Page(models.Model):

    name = models.CharField(max_length=50)
    page = models.IntegerField()
    page_image = models.ImageField()
    # image_mobile = models.ImageField(null=True)
    # image_desktop = models.ImageField(null=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)