from django.db import models

class Note(models.Model):

	COLORS = (
		('R', 'Red'),
		('B', 'Blue'),
		('O', 'Orange'),
		('Y', 'Yellow'),
		('G', 'Gray'),
		('W', 'White'),
	)

	title = models.CharField(max_length=100, blank=False)
	content = models.TextField(blank=False)
	date = models.DateField(auto_now=False, auto_now_add=True, blank=False)
	color = models.CharField(max_length=1, choices=COLORS, default='W')

	class Meta(object):
		verbose_name = "Note"
		verbose_name_plural = "Notes"
			

	def __unicode__(self):
		return self.title

