from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import Q
from ygnyoga.models import Ygnyoga
from blogs.models import Blogs, BlogMedia 
from .models import Classes,MondayClass,SundayClass,TuesdayClass,WednesdayClass,ThursdayClass,FridayClass,SaturdayClass
from .form import CreateClass,DeleteClass
from django.contrib import messages
import random

def classes(request):
    bloglist = list(Blogs.objects.all())
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    classes_cov = Ygnyoga.objects.filter(title="classes")
    context = {
        'classes': Classes.objects.all(), 
        'practic_classes' :Classes.objects.filter(class_type="Practice"),
        'workshop_classes' :Classes.objects.filter(class_type="workshop"),
        'random_blog_img' : random_blog,
        'class_info': classes_cov
    }
    return render(request, 'classes/classes.html',context)

def classschedule(request):
    classes_cov = Ygnyoga.objects.filter(title="classes")
    context = {
        'sunday' : SundayClass.objects.all(),
        'monday' : MondayClass.objects.all(),
        'tuesday' : TuesdayClass.objects.all(),
        'wednesday' : WednesdayClass.objects.all(),
        'thursday' : ThursdayClass.objects.all(),
        'friday' : FridayClass.objects.all(),
        'saturday' : SaturdayClass.objects.all(),
        'class_info': classes_cov
    }
    return render(request,'classes/schedule.html',context)

def classdetail(request,id):
    classimg = list(Classes.objects.all())
    random_classes = random.sample(classimg, 1) if len(classimg) >= 1 else classimg
    classes_cov = Ygnyoga.objects.filter(title="classes")
    
    bloglist = list(Blogs.objects.all())
    blog_media = BlogMedia.objects.filter(
        Q(upload_file__iendswith='.jpg') |
        Q(upload_file__iendswith='.jpeg') |
        Q(upload_file__iendswith='.png') |
        Q(upload_file__iendswith='.gif')
    )
    random_blog = random.sample(list(blog_media), 4) if len(blog_media) >= 4 else list(blog_media)
    context = {
        'classes' :Classes.objects.filter(classes_id=id).first(),
        'lest_classes' :Classes.objects.order_by('-classes_id')[:3],
        'blogs' :Blogs.objects.all(),
        'random_blog_img' : random_blog,
        'random_classes_img' : random_classes,
        'class_info': classes_cov

    }
    return render(request,'classes/classdetail.html',context)

def classcreate(request):
    if request.method == "POST": 
        form = CreateClass(request.POST,request.FILES) 
        select_day = request.POST.getlist("class_day")
        if form.is_valid(): 
            title = form.cleaned_data['title'] 
            short_des = form.cleaned_data['short_des'] 
            class_start_date = form.cleaned_data['class_start_date'] 
            class_end_date = form.cleaned_data['class_end_date'] 
            class_start_time = form.cleaned_data['class_start_time'] 
            class_end_time = form.cleaned_data['class_end_time'] 
            class_type = form.cleaned_data['class_type']
            instructor = form.cleaned_data['instructor']
            if instructor == 'Other':
                instructor = form.cleaned_data['other_instructor']

        if form.is_valid(): 
            classes = form.save(commit=False) 
            classes.save() 
            for day in select_day:
                if day == "Sunday":
                    dayclass = SundayClass
                    classDay(title,classes,dayclass)

                if day == "Monday":
                    dayclass = MondayClass
                    classDay(title,classes,dayclass)
                
                if day == "Tuesday":
                    dayclass = TuesdayClass
                    classDay(title,classes,dayclass)
                
                if day == "Wednesday":
                    dayclass = WednesdayClass
                    classDay(title,classes,dayclass)

                if day == "Thursday":
                    dayclass = ThursdayClass
                    classDay(title,classes,dayclass)
                
                if day == "Friday":
                    dayclass = FridayClass
                    classDay(title,classes,dayclass)

                if day == "Saturday":
                    dayclass = SaturdayClass
                    classDay(title,classes,dayclass)
                    
            messages.success(request, "Your class has been submitted.") 
            return redirect("/") 
    else: 
        form = CreateClass() 
    return render(request, "classes/classcreate.html", {"form": form})

def classDay(title,classes,dayclass):
    dayclass.objects.create(
        title = title,
        class_id = classes
    )


def classdelete(request,classes_id):
    class_delete = get_object_or_404(Classes, classes_id=classes_id)
    if request.method == "POST": 
        class_delete.delete()
        return redirect("/classes/classeslist/")
    else: 
        form = DeleteClass(instance=class_delete) 
    return render(request, "classes/classdelete.html", {"form": form,"class-delete":class_delete})


def lists_classes(request):
    classes = Classes.objects.all();
   # print(classes)
    return render(request,'classes/classlist.html',{'classes':classes})