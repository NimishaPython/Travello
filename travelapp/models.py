from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    number=models.IntegerField()
    desc=models.TextField()
    offer=models.BooleanField(default=False)


