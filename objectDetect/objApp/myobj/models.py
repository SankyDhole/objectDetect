from django.db import models

# Create your models here.
class object_store(models.Model):

    image_name = models.CharField(max_length=100, null=True)
    object_detail = models.JSONField(null=True)
    uploadtime = models.DateTimeField(null=True)

class uploadFile(models.Model):
    xml_file = models.FileField(upload_to='')
    img_file = models.ImageField(upload_to='')
