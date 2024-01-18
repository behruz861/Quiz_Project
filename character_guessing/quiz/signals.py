from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Journal

@receiver(post_save, sender=User)
def create_journal(sender, instance, created, **kwargs):
    if created:
        Journal.objects.create(user=instance)

@receiver(post_save, sender=Journal)
def save_journal(sender, instance, **kwargs):
    user_journal = instance.user.journal
    user_journal.correct_answers += instance.correct_answers
    user_journal.incorrect_answers += instance.incorrect_answers
    user_journal.save()
