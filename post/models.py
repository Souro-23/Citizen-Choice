from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .no_of_hashing import split

# Create your models here.

class PostsArticle(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default= timezone.now)
    abstract = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to=('images/'),blank=True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    hash_tags = models.CharField(max_length = 50,blank=  True)

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def summary(self):
        return self.absract[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    # def link_tags(self):
    #     cleaned_data = super().link_tags()
    #     tags = cleaned_data.get['hash_tags']
    #     tags = split(tags)
    #     for tag in tags:
    #         hashing(tag,"PostsArticle")
    #         hashing.create_link(tag,"PostsArticle")
    #     return cleaned_data

class FeedPosts(models.Model):
    body = models.TextField(max_length=300)
    image = models.ImageField(upload_to=('images/'),blank=True)
    pub_date = models.DateTimeField(default= timezone.now)
    user = models.ForeignKey(User , on_delete = models.CASCADE)



    def get_absolute_url(self):
        return reverse('home')
