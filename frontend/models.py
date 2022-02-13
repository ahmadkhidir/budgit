from tabnanny import verbose
from django.db import models


class Intro(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "intro"


class AboutUs(models.Model):
    heading = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name_plural = "about us"


class WhatWeDo(models.Model):
    icon = models.ImageField(upload_to="images")
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_image(self):
        return self.icon.url

    class Meta:
        verbose_name_plural = "what we do (s)"


class People(models.Model):
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    content = models.TextField()

    def get_image(self):
        return self.image.url

    class Meta:
        verbose_name_plural = "peoples"


class Contact(models.Model):
    address_link = models.CharField(max_length=500)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)


    class Meta:
        verbose_name_plural = "contact"

