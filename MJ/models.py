from django.db import models

# Create your models here.
# from django.db import models

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length = 120)
    reg_no = models.IntegerField(default=0)
    message = models.TextField(default='best')
