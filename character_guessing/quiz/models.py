from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Question(models.Model):
    image = models.ImageField(upload_to='questions/')
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='liked_questions')
    views = models.PositiveIntegerField(default=0)

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    total_tests = models.PositiveIntegerField(default=0)
    correct_answers = models.PositiveIntegerField(default=0)
    incorrect_answers = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    perfect_tests = models.PositiveIntegerField(default=0)
    success_percentage = models.PositiveIntegerField(default=0)

@receiver(post_save, sender=Journal)
def update_journal_stats(sender, instance, **kwargs):
    if instance.total_tests > 0:
        instance.success_percentage = (instance.correct_answers / instance.total_tests) * 100
    else:
        instance.success_percentage = 0
    instance.save()
