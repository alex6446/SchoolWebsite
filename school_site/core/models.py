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
	image = models.ImageField(default='about_pics/default.png', upload_to='about_pics')
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

class Schedule(models.Model):
	general = 'general'
	extra = 'extra'
	TYPES = (
		(general, "general"),
		(extra, "extra"),
		)
	table_type = models.CharField(max_length=25, choices=TYPES, default=general)
	table = models.FileField(upload_to="schedule_tables")

	def __str__(self):
		return self.table_type

