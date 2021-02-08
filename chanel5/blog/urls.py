from django.urls import path, re_path
from blog import views

app_name = "blog"
urlpatterns = [
    #Ex : /blog/
    path("", views.PostLV.as_view(), name="index"),
    
    #Ex : /blog/post/
    path("post/", views.PostLV.as_view(), name="post_list"),

    #Ex : /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name="post_detail"),

    #Ex : /blog/archive/
    path("archive/", views.PostAV.as_view(), name="post_archive"),
    
    #Ex : /blog/archive/2019
    path("archive/<int:year>/", views.PostYAV.as_view(), name="post_year_archive"),
    
    #Ex : /blog/archive/2019/nov
    path("archive/<int:year>/<str:month>/", views.PostMAV.as_view(), name="post_month_archive"),
    
    #Ex : /blog/archive/2019/nov
    path("archive/<int:year>/<str:month>/<int:day>/", views.PostDAV.as_view(), name="post_day_archive"),

    #Ex : /blog/archive/today
    path("archive/today/", views.PostTAV.as_view(), name="post_today_archive"),
    
]
