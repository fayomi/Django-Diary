from django.db import models

# Create your models here.
class Entry(models.Model):
    text = models.TextField()
    #this automatically sets the time when you create a new object
    date_posted = models.DateTimeField(auto_now_add=True)

    #this is a text representation of each object
    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'
