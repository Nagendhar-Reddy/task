from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django_comments.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User




class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Grade(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Availability(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('sickness', 'Sickness'),
        # Add more choices as needed
    ]

    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class YourModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='images/',blank=True,null=True)
    comments = GenericRelation(Comment)
    
    def __str__(self):
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def mark_as_read(self):
        self.read_at = timezone.now()
        self.save()

    def __str__(self):
        return self.subject
    
class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipient = models.EmailField()

    def __str__(self):
        return self.subject
    
class Agenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
    
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content}"
    
class SupportQuestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
    
