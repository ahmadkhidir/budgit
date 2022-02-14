from django.shortcuts import render
from django.views import View
from .models import Intro, AboutUs, WhatWeDo, People, Contact
from django.conf import settings


class HomeView(View):
    def get(self, request, lang=settings.LANGUAGE_CODE):
        intro = Intro.objects.last()
        about = AboutUs.objects.last()
        what_we_do = WhatWeDo.objects.all()
        people = People.objects.all()
        contact = Contact.objects.last()

        context = {
            "lang": lang,
            "languages": settings.LANGUAGES,
            "intro": intro,
            "about": about,
            "what_we_do": what_we_do,
            "people": people,
            "contact": contact,
        }
        return render(request, "frontend/home_page.html", context)
