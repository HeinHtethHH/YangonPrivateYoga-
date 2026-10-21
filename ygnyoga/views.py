import random
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Ygnyoga
from blogs.models import Blogs,BlogMedia
from classes.models import Classes
from user.models import CustomUser

def welcome(request):
    bloglist = list(Blogs.objects.all())
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    welcome = Ygnyoga.objects.filter(title="Welcome")
   
    context = {
        'welcome_info' : welcome,
        'blogs' :Blogs.objects.order_by('-post_datetime')[:3],
        'lest_classes' :Classes.objects.order_by('-classes_id')[:3],
        'random_blog_img' : random_blog,
        'users': CustomUser.objects.exclude(role__in=["ceo","consultant","normal", "guest","admin"]), 
        'instructor_info': CustomUser.objects.filter(role='instructor')        
    }
    return render(request,'ygnyoga/welcome.html',context)


def about(request):
    bloglist = list(Blogs.objects.all())
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    about =  Ygnyoga.objects.filter(title="About")

    user_instructor = CustomUser.objects.filter(role__contains='instructor').order_by('id')   # or order_by('blog_id')
    paginator = Paginator(user_instructor, 3)  #  blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
         'about_info' : about,
         'ceo_info':CustomUser.objects.filter(role__contains='CEO'),
         'consultant_info':CustomUser.objects.filter(role__contains='consultant'),
         'instructor_info': page_obj,
         'random_blog_img' : random_blog,
    }
    return render(request,'ygnyoga/about.html',context)
