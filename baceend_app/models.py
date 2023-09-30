from django.db import models

# Create your models here.
class Enroll(models.Model):
    Name = models.TextField(max_length=150)
    Email =models.EmailField()
    MobileNumber = models.CharField(max_length=10,null=True)
    Course = models.TextField(max_length=150,)

    def __str__(self):
        return self.Name


