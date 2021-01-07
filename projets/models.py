from django.db import models


class Projets(models.Model):
    titre=models.CharField(max_length=50)
    description=models.TextField()
    url_image=models.CharField(max_length=2000)
