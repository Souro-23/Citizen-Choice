from django.urls import path
from . import views as friend_views


urlpatterns = [
		path('friend-request/send/<pk>',friend_views.send_friend_request,name='request-send'),
        path('friend-request/accept/<pk>',friend_views.accept_friend_request,name='request-accept'),
        path('friend-request/cancel/<pk>',friend_views.cancel_friend_request,name='request-cancel'),
    	path('friend-request/delete/<pk>',friend_views.delete_friend_request,name='request-delete'),


    	path('user_profile/<slug>', friend_views.profile_view,name='profile'),
		]