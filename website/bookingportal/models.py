from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):


    field_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slot = models.CharField(max_length=10)
    roll_number = models.IntegerField(null=True, blank=True)
    ca = models.CharField(max_length=50, blank=True)
    approvedby_ca = models.NullBooleanField(default = False)
    approvedby_chairman = models.NullBooleanField(default = False)
    is_booked = models.BooleanField(default = False)
    comments_ca = models.CharField(max_length=500, blank=True)
    comments_chairman = models.CharField(max_length=500, blank=True)
    date_modified = models.DateTimeField(auto_now = True)


    #def __str__(self):
    #    return f'{self.name} {self.date}'

    def short_description(self):
        return self.description[:15]

    #def __str__(self):
    #    return self.author

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    roll_number = models.IntegerField(null=True, blank=True)
    branch = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    course = models.CharField(max_length=10)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
