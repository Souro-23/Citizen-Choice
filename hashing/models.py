from django.db import models
from post.models import PostsArticle, FeedPosts
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class hash_tags(models.Model):
        hash = models.CharField(max_length = 20,null = True)

        @classmethod
        def create_link(cls,tag):
              hash_tag, created = cls.objects.get_or_create(
              hash = tag )
              if created:
                  hash_tag.hash = tag
                  hash_tag.save()
              return hash_tags.objects.get(hash = tag)


class hashing(models.Model):
    tag_id = models.ForeignKey(hash_tags ,related_name="tag",
                                        on_delete = models.CASCADE,null = True)
    field_id = models.ForeignKey(ContentType ,related_name="field",
                                          on_delete=models.CASCADE,null = True)
    object_id = models.IntegerField(null = True)
