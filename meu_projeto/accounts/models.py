from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    security_question = models.CharField(max_length=255, default="Qual o nome da sua cidade natal?")
    security_answer = models.CharField(max_length=255)  

    def save(self, *args, **kwargs):
        self.security_answer = hashlib.sha256(self.security_answer.encode()).hexdigest()
        super().save(*args, **kwargs)

    def check_answer(self, answer):
        return hashlib.sha256(answer.encode()).hexdigest() == self.security_answer
    


