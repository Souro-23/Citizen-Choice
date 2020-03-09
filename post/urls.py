from django.urls import path, include
from . import views
from .views import PostUpdateView , PostCreateView, PostCreateFeedView, FeedUpdateView

urlpatterns = [


  path('<int:pk>/update',PostUpdateView.as_view(), name='edit_post'),
  path('<int:pk>/updateFeed',FeedUpdateView.as_view(), name='edit_Feed'),
  path('create/article',PostCreateView.as_view(), name='post-create'),
  path('create/feed',PostCreateFeedView, name='post-createFeed'),
]
