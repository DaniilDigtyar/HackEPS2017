from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    followers=models.IntegerField()
    follows=models.IntegerField()
    facebook_vinculado=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Photos(models.Model):
    idphoto=model.IntegerField(primary_key=True)
    username_vinculed=model.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.IntegerField()
    coments=models.IntegerField()
    hastags=TextField()

    def __str__(self):
        return self.title
# Create your models here.
