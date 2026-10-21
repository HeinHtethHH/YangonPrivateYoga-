from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('register/',request_signup,name='user-register'),
    path('appdeluser/',appdeluser,name='app_del_user'),
    path('<str:pk>/approve/',approve_requser,name='requser-approve'),
    path('<str:pk>/delete/',delete_requser,name='requser-delete'),
    path('<str:pk>/edit/',edit_user,name='user-edit'),
    path('userlists/',lists_users,name='users_lists'),
    path('login/',auth_view.LoginView.as_view(template_name='user/login.html'),name="user-login"),
    path('logout/',auth_view.LogoutView.as_view(template_name="user/logout.html"),name="user-logout"),
    path('profile/',profile,name='user-profile'),
    path('profile/update/',userinfoupdate,name='user-info-update'),
    path('profile/image/update/',userphotoupdate,name='user-image-update'),
]