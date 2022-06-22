from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Books(models.Model):
    isbn = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    author = models.TextField(blank=True, null= True)
    publisher = models.CharField(max_length=250)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=(('Available','Available'), ('Not Available','Not Available')), default = 'Available')
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "List of Books"

    def __str__(self):
        return str(f"{self.isbn} - {self.title}")