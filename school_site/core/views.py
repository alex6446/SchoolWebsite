import pandas
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import (
 	About,
	Event,
	News,
	Teacher,
	Timetable,
	Schedule,
	Contact,
	Gallery,
	GalleryImage,
	Background,
	)
from .forms import ContactForm


def home(request):
	news_list = News.objects.all().order_by('-date_posted')
	paginator = Paginator(news_list, 3)
	page = request.GET.get('page')
	pNews = paginator.get_page(page)

	event_list = Event.objects.all().order_by('-date_posted')
	paginator = Paginator(event_list, 2)
	pEvent = paginator.get_page(page)

	background_list = Background.objects.filter(page='home')
	try:
		background_home = background_list[0].image
	except:
		background_home = None

	context = {
		'events': pEvent,
		'about': About.objects.all(),
		'news': pNews,
		'title': 'Home',
		'changebg': True,
		'background_home': background_home,
	}
	return render(request, 'core/home.html', context)

def about(request):
	context = {
		'title': 'About',
		'about': About.objects.all(),
		'teachers': Teacher.objects.all(),
	}
	return render(request, 'core/about.html', context)

def gallery(request):
	gallery_list = Gallery.objects.all().order_by('-date_posted')
	paginator = Paginator(gallery_list, 2)
	page = request.GET.get('page')
	pGallery = paginator.get_page(page)
	context = {
		'title': 'Gallery',
		'gallery': pGallery,
		'changebg': True,
	}
	return render(request, 'core/gallery.html', context)

def schedule(request):
	context = {
		'title': 'Schedule',
		#'tables': HtmlScheduleTables,
		'lessons': Schedule.objects.all(),
		'time': Timetable.objects.all(),
	}
	return render(request, 'core/schedule.html', context)

def students(request):
	context = {
		'title': 'Students',
	}
	return render(request, 'core/students.html', context)

def news(request):
	news_list = News.objects.all().order_by('-date_posted')
	paginator = Paginator(news_list, 4)
	page = request.GET.get('page')
	pNews = paginator.get_page(page)

	context = {
		'title': 'News',
		'events': Event.objects.all().order_by('-date_posted'),
		'news': pNews,
		'changebg': True,
	}
	return render(request, 'core/news.html', context)

def contacts(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# send email
			sender_name = form.cleaned_data['name']
			sender_email = form.cleaned_data['email']

			message = "{0} has sent you a message:\n\n{1}".format(sender_name, 
				form.cleaned_data['message'])
			send_mail('New Enquiry', message, sender_email, 
				[settings.EMAIL_HOST_USER])

			messages.success(request, f'Message sent!')
			return redirect('core-contacts')
	else:
		form = ContactForm()

	context = {
		'title': 'Contacts',
		'form': form,
		'info': Contact.objects.all()
	}
	return render(request, 'core/contacts.html', context)

class news_detail(DetailView):
	model = News
	
class event_detail(DetailView):
	model = Event

class teacher_detail(DetailView):
	model = Teacher

class gallery_detail(DetailView):
	model = Gallery
