from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=300,null=True)
    email = models.EmailField(null=True,unique=True)
    bio = models.TextField(null=True)
    avatar= models.ImageField(null=True,default="3.jpg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    # def __str__(self):
    #     return self.name

class Topic(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True) # "null attribute for database" and "blank attribute for form"
    participants = models.ManyToManyField(User,related_name='participants',blank=True)
    updated_time = models.DateTimeField(auto_now=True) # takes snapshot everytime we save an item
    created_time = models.DateTimeField(auto_now_add=True) # take a snapshot the moment it is created. Just once, not everytime

    class Meta:
        ordering = ['-updated_time','-created_time']


    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    updated_time = models.DateTimeField(auto_now=True) # takes snapshot eveyrtime we save an item
    created_time = models.DateTimeField(auto_now_add=True) #


    class Meta:
        ordering = ['-updated_time','-created_time']

    def __str__(self):
        return self.body[0:20]

