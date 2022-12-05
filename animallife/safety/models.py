from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    user_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    begin_timestamp = models.CharField(max_length=305)
    end_timestamp = models.CharField(max_length=305)
    def __str__(self):
        return self.title

class AnimalUsers(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username

