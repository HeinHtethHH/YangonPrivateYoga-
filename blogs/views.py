
from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import Q
from ygnyoga.models import Ygnyoga
from .models import Blogs,Category,Albums, BlogMedia
from .form import PostForm, BlogMediaFormSet, CreateAlbumForm
from django.contrib import messages
from django.core.paginator import Paginator
import random

def postblogs(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            blog_instance = form.save()
            formset = BlogMediaFormSet(request.POST, request.FILES, instance=blog_instance)
            if formset.is_valid():
                formset.save()
            return redirect('/')
    else:
        form = PostForm()
        formset = BlogMediaFormSet(instance=Blogs()) # ဒါက အလွတ်ပုံစံ ၃ ခု ပြပေးမှာပါ
        
    return render(request, 'blogs/newblog.html', {
        'form': form, 
        'formset': formset # Template ထဲမှာ {{ formset }} လို့ သုံးထားတဲ့ နာမည်နဲ့ ကိုက်ရပါမယ်
    })

############################################

def blogs(request):
    blogs = Blogs.objects.all().order_by('-date')   # or order_by('blog_id')
    paginator = Paginator(blogs, 6)  # 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    blogs =  Ygnyoga.objects.filter(title="blog")
    context = {
        'blogs': page_obj,
        'random_blog_img': random_blog,
        'blog_info': blogs
    }
    return render(request, 'blogs/post.html', context)

############################################

def blogdetail(request,code):
    blogs = Blogs.objects.all().order_by('-date')
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    ygn_blogs =  Ygnyoga.objects.filter(title="blog")
    context = {
        'blog_detail' :Blogs.objects.get(blog_id=code),
        'blogs' :Blogs.objects.order_by('-post_datetime')[:6],
        'random_blog_img' : random_blog,
        'categories':Category.objects.all(),
        'blog_info': ygn_blogs
    }
    
    return render(request,'blogs/postdetail.html',context)
############################################

def gallery(request):
    blogs_data = BlogMedia.objects.all().order_by('id')   # or order_by('blog_id')
    blogs = blogs_data.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    paginator = Paginator(blogs, 9)  # 9 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    blogs =  Ygnyoga.objects.filter(title="blog")
    context = {
        'blogs': page_obj,
        'blog_info': blogs
    }
    return render(request, 'blogs/gallery.html', context)
##################################################

def createalbum(request):
    if request.method == "POST":
        form = CreateAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateAlbumForm()
    return render(request, "blogs/createalbum.html",{'form':form})
#################################################
def albums(request):
    albums = Albums.objects.all()
    albums_cov = Ygnyoga.objects.filter(title="blog")
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    context = {
        'albums': albums, 
        'albums_info': albums_cov,
        'random_blog_img': random_blog,
    }
    return render(request, 'blogs/albums.html',context)
#################################################
def albumDetail(request,code):
    # album_detail = Albums.objects.get(albums_id = code) 
    blogs = Blogs.objects.filter(albums__albums_id=code).order_by('-date')
    if not blogs:
        blogs = Blogs.objects.filter(albums__isnull=True).order_by('-date')

    paginator = Paginator(blogs, 6)  # 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    blogs =  Ygnyoga.objects.filter(title="blog")
    context = {
        'blogs': page_obj,
        'random_blog_img': random_blog,
        'blog_info': blogs
    }
    return render(request, 'blogs/post.html', context)