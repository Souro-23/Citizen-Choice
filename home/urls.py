from django.urls import path
from .views import HomeView, history
from user_profile.views import createProfile

urlpatterns = [
		path('',HomeView.as_view(),name='home'),

		path('create-profile/',createProfile,name='createProfile'),
		path('history/', history, name='history')


]
