from django.shortcuts import render
from blog import models
from django.views.generic import ListView, DetailView
from django.views.generic.ArchiveIndexView import
# Create your views here.

class PostLV(ListView):
    model = Bookmark
    
class PostDV(DetailView):
    model = Bookmark

class PostYAV():

class PostMAV():

class PostDAV():

class PostTAV():