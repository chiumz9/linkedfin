from django.db import models
from django.forms import DateTimeField
from datetime import datetime
from user_profile.models import User_profile


class Project(models.Model):
    user_id = models.ForeignKey(User_profile, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=128)
    github_link = models.CharField(max_length=128)
    publish_date = models.DateTimeField(datetime.now())
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title