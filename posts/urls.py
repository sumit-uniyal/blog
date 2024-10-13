from django.urls import path, include
from .views import *
from .ajax import *

urlpatterns = [
    path('', home, name='home'),
    path('ajax', dynamic_ajax, name="dynamic_ajax"),
    path('blog_detail/<int:id>/', blog_detail, name="blog_detail"),
    path('comment_like/<int:id>/', comment_like, name="comment_like"),
    path('blog/<int:blog_id>/share/', share_blog, name='share_blog'),
]