from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .models import hash_tags, hashing
from .seperate_tags import seperate_tags

# Create your views here.
def create_hash(tag,post_id,field):
    field_id = ContentType.objects.get( model = field )
    hash_tag_ids = create_tag(tag)
    for id in hash_tag_ids:
        hash = hashing()
        hash.tag_id = id
        hash.field_id = field_id
        hash.object_id = post_id
        hash.save()
    return


def create_tag(tag):
    tags = seperate_tags(tag)
    id = []
    for tag in tags:
        tag_name = hash_tags()
        tag_name = tag_name.create_link(tag)
        id += [tag_name]
    return id
