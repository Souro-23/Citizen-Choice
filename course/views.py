from .forms import CourseForm,TopicFormset,Sub_TopicFormset,Sub_TopicForm
from .models import courses,topics,sub_topics
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class Create_Course_View(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    model = courses
    form_class = CourseForm
    template_name = 'course/add.html'
    success_url = 'course/add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        result = super(Create_Course_View, self).form_valid(form)

        topic_formset = TopicFormset(form.data, instance=self.object, prefix='topic_formset')

        if topic_formset.is_valid():
            for topic in topic_formset:
                topic.instance.user = self.request.user
            topics = topic_formset.save()

        topics_count = 0

        for topic in topics:
            sub_topic_formset = Sub_TopicFormset(form.data, instance = topic, prefix='sub_topic_formset_%s'% topics_count)
            x = sub_topic_formset.cleaned_data[0]
            sub = sub_topics()

            files = self.request.FILES

            if sub_topic_formset.is_valid():
                sub.name = x['name']
                sub.content = x['content']
                sub.sno = x['sno']
                try:
                  sub.image = files['sub_topic_formset_%s-%s-image'%(topics_count,x['sno'])]
                except:
                    sub.image = []

                try:
                    sub.pdf = files['sub_topic_formset_%s-%s-pdf'%(topics_count,x['sno'])]
                except:
                    sub.pdf = []
                sub.topic = x['topic']
                sub.user = self.request.user
                sub.save()

        return result

    def get_context_data(self, **kwargs):
        context = super(Create_Course_View, self).get_context_data(**kwargs)
        context['topic_formset'] = TopicFormset(prefix='topic_formset')
        context['sub_topic_formset'] = Sub_TopicFormset(prefix='sub_topic_formset_0')
        # context['image'] = upload_image
        # print(upload_image)
        return context
