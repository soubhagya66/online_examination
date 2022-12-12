from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True)
    address = models.CharField(max_length=40)
    # mobile = models.CharField(max_length=20,null=False)
    mobile = models.IntegerField()
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
