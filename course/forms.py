from django.forms import ModelForm, HiddenInput, Form
from django.forms import formset_factory, inlineformset_factory,modelformset_factory
from .models import courses, topics, sub_topics, course_to_topics, topics_to_subtopics
from django import forms
class CourseForm(ModelForm):
    class Meta:
        model = courses
        fields = ['name',]
        exclude = ()


class TopicForm(ModelForm):
    class Meta:
        model = topics
        fields = ['name',]
        exclude = ('course',)


class Sub_TopicForm(Form):
    name  = forms.CharField(max_length = 50)
    content = forms.CharField(max_length = 50)
    sno   = forms.IntegerField()
    image = forms.ImageField()
    pdf = forms.FileField()

TopicFormset = inlineformset_factory(courses, topics, fields=('name','sno'),extra =1,widgets = {'sno': HiddenInput()})
Sub_TopicFormset = inlineformset_factory(topics, sub_topics, fields=('name','content','sno','image','pdf'),extra = 1,widgets = {'sno': HiddenInput()})
