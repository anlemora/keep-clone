from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=100, blank=False)
	content = models.TextField(blank=False)
	date = models.DateField(auto_now=False, auto_now_add=True, blank=False)

	class Meta(object):
		verbose_name = "Note"
		verbose_name_plural = "Notes"
			

	def __unicode__(self):
		return self.title

