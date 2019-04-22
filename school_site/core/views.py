from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import About
from .models import Event
from .models import News
from .models import Teacher


def home(request):
	news_list = News.objects.all().order_by('-date_posted')
	paginator = Paginator(news_list, 3)
	page = request.GET.get('page')
	pNews = paginator.get_page(page)

	event_list = Event.objects.all().order_by('-date_posted')
	paginator = Paginator(event_list, 2)
	pEvent = paginator.get_page(page)

	AboutArticles = About.objects.all()
	context = {
		'events': pEvent,
		'welcome': AboutArticles[0],
		'news': pNews,
		'title': 'Home'
	}
	return render(request, 'core/home.html', context)

def about(request):
	AboutArticles = About.objects.all()
	context = {
		'title': 'About',
		'welcome': AboutArticles[0],
		'history': AboutArticles[1],
		'teachers': Teacher.objects.all(),
	}
	return render(request, 'core/about.html', context)

def schedule(request):
	context = {
		'title': 'Schedule',
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
	}
	return render(request, 'core/news.html', context)

"""
class NewsListView(ListView):
	model = News
	template_name = 'core/news.html'
	context_object_name = 'news'
	ordering = ['-date_posted'] 
	paginate_by = 2
	def get_queryset(self):
		return News.objects.all()
	def get_context_data(self, **kwargs):
		context = super(NewsListView, self).get_context_data(**kwargs)
		context.update({
			'events': Event.objects.all(),
			#'news': News.objects.all(),
			'title': 'News',
			})
		return context
"""

def contacts(request):
	context = {
		'title': 'Contacts',
	}
	return render(request, 'core/contacts.html', context)

class news_detail(DetailView):
	model = News
	
class event_detail(DetailView):
	model = Event

class teacher_detail(DetailView):
	model = Teacher
