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
    followers = models.ManyToManyField("auth.User", related_name="user_followers")
    created = models.DateTimeField(auto_now_add=True)
    suggestions = models.ManyToManyField("auth.User", related_name="user_suggestions")


class Alcohol(models.Model):
    alcohol_type = models.CharField(max_length=20)

    def __str__(self):
        return self.alcohol_type


class Like(models.Model):
    user = models.CharField(max_length=30)


class Suggestion(models.Model):
    title = models.CharField(max_length=30, blank=True)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User")
    alcohol = models.ManyToManyField(Alcohol)
    likes = models.ManyToManyField(Like, related_name="user_likes")

    class Meta:
        ordering = ["-created"]

