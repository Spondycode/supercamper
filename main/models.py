from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "/n" + self.description


class Profile(models.Model):
    class CampTypes(models.TextChoices):
        SMALL_TENT = "Tent"
        BIG_TENT = "Big Tent"
        SMALL_VAN = "Small Van"
        MED_VAN = "Medium Van"
        CAMPER = "Camper"
        LARGE_CAMPER = "Large Camper"

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=150)
    camper_type = models.CharField(max_length=15, choices=CampTypes.choices)
    image = models.ImageField(upload_to='uploads/profile_pics/')
    favourite = models.CharField(max_length=200)

    def __str__(self):
        return self.name



#Create Profile when new user signs up

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

    post_save.connect(create_profile, sender=User)
