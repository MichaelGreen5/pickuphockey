from django.db import models

class UploadSheet(models.Model):
    file = models.FileField(upload_to='OrgDash/uploads/')

# Create your models here.
