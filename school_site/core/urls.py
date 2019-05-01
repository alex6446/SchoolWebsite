from django.urls import path
from . import views
from .views import (
	news_detail, 
	event_detail,
	teacher_detail,
    gallery_detail, 
	#NewsListView,
	)

urlpatterns = [
    path('', views.home, name='core-home'),
    path('about/', views.about, name='core-about'),
    path('gallery/', views.gallery, name='core-gallery'),
    path('schedule/', views.schedule, name='core-schedule'),
    path('students/', views.students, name='core-students'),
    #path('news/', NewsListView.as_view(), name='core-news'),
    path('news/', views.news, name='core-news'),
    path('contacts/', views.contacts, name='core-contacts'),
    path('post/<int:pk>/', news_detail.as_view(), name='news-detail'),
    path('event/<int:pk>/', event_detail.as_view(), name='event-detail'),
    path('teacher/<int:pk>/', teacher_detail.as_view(), name='teacher-detail'),
    path('gallery/<int:pk>/', gallery_detail.as_view(), name='gallery-detail'),
]