from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "postsVlue"
    paginate_by = 2
    
class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    detail_field = "modify_dt"

class PostYAV(YearArchiveView):
    model = Post
    detail_field = "modify_dt"
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    detail_field = "modify_dt"

class PostDAV(DayArchiveView):
    model = Post
    detail_field = "modify_dt"

class PostTAV(TodayArchiveView):
    model = Post
    detail_field = "modify_dt"