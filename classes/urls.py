from django.urls import path
from .views import *

urlpatterns = [
    path('',classes,name='all-classes'),
    path('schedule/',classschedule,name='classes-schedule'),
    path('<str:id>/detail/',classdetail,name='class-detail'),
    path('newclass/',classcreate,name='class-new'),
    path('<str:classes_id>/delete/',classdelete,name='class-delete'),
    path('classeslist/',lists_classes,name='class-list')
]