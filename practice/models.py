from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    username = models.CharField(max_length = 20)
    follows  = models.ManyToManyField('self', symmetrical=False)
    def __str__(self):
        return self.username

class posts(models.Model):
    user      = models.ForeignKey(profile, on_delete=models.CASCADE)
    post_text = models.TextField()
    def __str__(self):
        return self.post_text
