from django.db import models


class Project(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    image_url=models.CharField(max_length=2000)
