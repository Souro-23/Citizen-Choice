from django import forms
from .no_of_hashing import split
from .models import PostsArticle

class Post_Article(forms.ModelForm):
    title = forms.CharField(label = 'Title',max_length = 100)
    abstract = forms.CharField(widget = forms.Textarea, max_length = 300)
    body = forms.CharField(widget = forms.Textarea)
    image = forms.ImageField(required = False)
    hash_tags = forms.CharField(max_length = 50,required = False)

    def clean(self):
        cleaned_data = super().clean()
        tags = cleaned_data.get("hash_tags")
        if tags:
          tags = split(str(tags))
          if len(tags) > 5:
            raise forms.ValidationError('Maximum 5 tags are allowed')
        return

    class Meta:
        model = PostsArticle
        fields=("title", "abstract", "body", "hash_tags", "image")
