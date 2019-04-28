from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import (
	News,
	About,
	Event,
	Teacher,
	Schedule,
	)


class CustomAdmin(admin.ModelAdmin):

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
		}
	
	"""class Media:
		js = (
			'js/tinymce/tinymce.min.js', # tinymce js file
			'js/tinymce/custom.js',       # project static folder
		)
		print("done")"""


admin.site.register(News, CustomAdmin)
admin.site.register(About, CustomAdmin)
admin.site.register(Event, CustomAdmin)
admin.site.register(Teacher, CustomAdmin)
admin.site.register(Schedule, CustomAdmin)

