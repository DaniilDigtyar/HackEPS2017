from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    followers = models.IntegerField(default=0)
    follows = models.IntegerField(default=0)
    facebook_link = models.CharField(max_length=200, default='')
    description = models.TextField(null=True)
    profile_pic_link = models.CharField(max_length=200, default='')
    crawler = models.CharField(max_length=200, default='')
    external_link = models.CharField(max_length=200, default='')
    scraped = models.BooleanField(default=False)
    parsed = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class FollowRelation(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='users')
    follower = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='qwe')


class Photos(models.Model):
    idphoto = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.IntegerField()
    hashtags = models.TextField(null=True, default='')

    def __str__(self):
        return '{}'.format(self.idphoto)
