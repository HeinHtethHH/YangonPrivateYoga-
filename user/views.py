from django.shortcuts import get_object_or_404, render,redirect
from .form import ReqUserApproveForm, UserRegister, ReqUserDeleteForm, ProfileForm,ProfileImgForm
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from .models import UserInap, CustomUser, Instructor, CustomUser
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


# def userinap(request):
#     return render(request,'user/usernap.html')
# # Create your views here.

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Register Success {username}!')
#             return redirect('/')
#     else:
#         form = RegisterForm()
#     return render(request, 'user/register.html')


def request_signup(request): 
    if request.method == "POST": 
        form = UserRegister(request.POST, request.FILES) 
        if form.is_valid(): 
            user_inap = form.save(commit=False) 
            user_inap.status = "pending" 
            user_inap.save() 
            messages.success(request, "Your request has been submitted.") 
            return redirect("/") 
    else: 
        form = UserRegister() 
    return render(request, "user/request_form.html", {"form": form})

@login_required
def appdeluser(request):
    userInap = UserInap.objects.all();
    return render(request,'user/approve_delete_user.html',{'userInap':userInap})

@login_required
def approve_requser(request, pk):
    user_inap = get_object_or_404(UserInap, pk=pk)

    if request.method == "POST":
        selected_role = request.POST.getlist("role")
        user_inap.status = "approved"
        user_inap.save()

        # Create CustomUser with same ID
        user = CustomUser.objects.create(
            id=user_inap.user_id,
            email=user_inap.email,
            username=user_inap.email,
            date_of_birth = user_inap.date_of_birth,
            image=user_inap.image,
            name=user_inap.name,
            phone=user_inap.phone,
            address=user_inap.address,
            bio=user_inap.bio,
            facebook = user_inap.facebook,
            instagram = user_inap.instagram,
            youtube = user_inap.youtube,
            tiktok = user_inap.tiktok,
            role=selected_role
        )
        if ("admin" in selected_role) or ("instructor" in selected_role): 
            user.is_staff = True 
        else: 
            user.is_staff = False 
            
        user.set_password(user_inap.password)  # hash password
        user.save()

        # Assign group based on role
        group, created = Group.objects.get_or_create(name=selected_role)
        user.groups.add(group)

        # Example: assign specific permission
        if "instructor" in selected_role:
            Instructor.objects.create(
                user=user, expertise="Yoga", # default or form input 
                bio=user_inap.bio 
            )
              # handle gracefully if permission not defined
            # Example: assign permission if exists 
            try: 
                perm = Permission.objects.get(codename="add_class") 
                user.user_permissions.add(perm) 
            except Permission.DoesNotExist: 
                pass

        # Delete UserInap record after approval 
        user_inap.delete()

        messages.success(request, f"{user_inap.name} approved as {selected_role}.")
        return redirect("/user/appdeluser/")
    else:
        form = ReqUserApproveForm(instance=user_inap)
    return render(request, "user/approve_requser.html", {"form": form})

@login_required
def delete_requser(request, pk):
    user_del_inap = get_object_or_404(UserInap, pk=pk)

    if request.method == "POST":
        user_del_inap.delete()
        messages.success(request, f"{user_del_inap.name} deleted successfully.")
        return redirect("/user/appdeluser/")
    else:
        form = ReqUserDeleteForm(instance=user_del_inap)
    return render(request, "user/delete_requser.html", {"form": form, "user_del_inap": user_del_inap})

@login_required
def lists_users(request):
    users = CustomUser.objects.all();
    print(users)
    return render(request,'user/user_lists.html',{'users':users})

@login_required
def edit_user(request, pk):
    return render(request, "user/edit_user.html")

# @login_required
# def profile(request):
#     userinfo = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=userinfo)
#         if form.is_valid():
#             form.save()
#             return redirect('user-profile')
#     else:
#         form = ProfileForm(instance=userinfo)

#     return render(request, 'user/userprofile.html', {
#         'userinfo': userinfo,
#         'form': form
#     })

@login_required
def profile(request):
    userinfo = request.user
    return render(request, 'user/userprofile.html', {
        'userinfo': userinfo,
    })

@login_required
def userinfoupdate(request):
    userinfo = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=userinfo)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = ProfileForm(instance=userinfo)

    return render(request, 'user/userinfoupt.html', {
        'userinfo': userinfo,
        'form': form
    })

@login_required
def userphotoupdate(request):
    userinfo = request.user
    if request.method == 'POST':
        form = ProfileImgForm(request.POST, request.FILES, instance=userinfo)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = ProfileImgForm(instance=userinfo)

    return render(request, 'user/profleimgupt.html', {
        'userinfo': userinfo,
        'form': form
    })
