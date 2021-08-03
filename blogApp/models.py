from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    slug = models.CharField(max_length=130)
    content = models.TextField(max_length=600)
    timestamp = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title

class  BlogComment(models.Model) :
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateField(default=now)

    def __str__(self):
        return self.comment[0:15]+"... by "+ self.user.username
    