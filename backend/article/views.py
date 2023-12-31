from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Member


def members(request):
    return HttpResponse("Hello world!")


def new_articles(request):
    member = Member(firstname="Emil", lastname="Refsnes")
    member.save()
    return HttpResponse("Hello world!")
