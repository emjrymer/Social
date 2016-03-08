from django.db import models


class Follower(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    age = models.IntegerField(null=True)
    name = models.CharField(max_length=25)
    favorite_alcohol = models.CharField(max_length=30)
    followers = models.ManyToManyField(Follower)
    created = models.DateTimeField(auto_now_add=True)


class Alcohol(models.Model):
    alcohol_type = models.CharField(max_length=20)

    def __str__(self):
        return self.alcohol_type


class Suggestion(models.Model):
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User")
    alcohol = models.ManyToManyField(Alcohol)

    class Meta:
        ordering = ["-created"]



