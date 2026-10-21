from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('post/newblog/',postblogs,name='post-blogs'),
    path('',blogs,name='all-blogs'),
    path('post/<slug:code>/detail',blogdetail,name='blog-detail'),
    path('gallery/',gallery,name='all-gallery'),
    path('post/createalbum',createalbum,name='create-album'),
    path('albums',albums,name='all-albums'),
    path('albums/<slug:code>/detail',albumDetail,name='album-detail')

]