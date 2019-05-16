from django.db import models
from django.utils import timezone


class News(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(default='news_pics/default.png', upload_to='news_pics')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class About(models.Model):
	welcome = 'welcome'
	history = 'history'
	TYPES = (
		(welcome, "welcome"),
		(history, "history"),
		)
	post_type = models.CharField(max_length=25, choices=TYPES, default=welcome)
	title = models.CharField(max_length=150)
	image = models.ImageField(default=None, upload_to='about_pics', blank=True)
	content = models.TextField()

	def __str__(self):
		return self.title

class Event(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(default='event_pics/default.png', upload_to='event_pics')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class Teacher(models.Model):
	photo = models.ImageField(default='teacher_photos/default.png', upload_to='teacher_photos')
	name = models.CharField(max_length=150)
	rank = models.CharField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.name

class Timetable(models.Model):
	general_summer = 'general_summer'
	general_winter = 'general_winter'
	extra = 'extra'
	TYPES = (
		(general_summer, "general_summer"),
		(general_winter, "general_winter"),
		(extra, "extra"),
		)
	title = models.CharField(max_length=150)
	table_type = models.CharField(max_length=25, choices=TYPES, default=general_summer)
	table = models.TextField()

	def __str__(self):
		return self.table_type

class Schedule(models.Model):
	general = 'general'
	extra = 'extra'
	TYPES = (
		(general, "general"),
		(extra, "extra"),
		)
	table_type = models.CharField(max_length=25, choices=TYPES, default=general)
	table = models.ImageField(upload_to="schedule_tables")

	def __str__(self):
		return self.table_type

class Contact(models.Model):
	title = models.CharField(max_length=150)
	information = models.TextField()

	def __str__(self):
		return self.title

class Gallery(models.Model):
	title = models.CharField(max_length=300)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class GalleryImage(models.Model):
	gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.SET_NULL, null=True)
	image = models.ImageField()

class AttachedFileNews(models.Model):
	file = models.FileField(upload_to="attached_files", blank=True)
	news = models.ForeignKey(News, related_name='news_files', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=300, default="Download")

class AttachedFileAbout(models.Model):
	file = models.FileField(upload_to="attached_files", blank=True)
	about = models.ForeignKey(About, related_name='about_files', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=300, default="Download")

class AttachedFileEvent(models.Model):
	file = models.FileField(upload_to="attached_files", blank=True)
	event = models.ForeignKey(Event, related_name='event_files', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=300, default="Download")

class AttachedFileTeacher(models.Model):
	file = models.FileField(upload_to="attached_files", blank=True)
	teacher = models.ForeignKey(Teacher, related_name='teacher_files', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=300, default="Download")

