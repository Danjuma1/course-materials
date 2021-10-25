from django.db import models

class Material(models.Model):
    course_code = models.CharField(max_length=8)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/materials')
    contributor = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Search(models.Model):
	search  = models.CharField(max_length=200, null=True)
	time  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.search

	class Meta:
		verbose_name_plural='Searches'