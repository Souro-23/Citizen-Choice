from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.models import Profile
from friends.models import FriendRequest

# Create your views here.


class HomeView(LoginRequiredMixin,TemplateView):
	login_url = '/login/'
	template_name = 'HomePage/index.html'
	def get(self,request):
		users = Profile.objects.exclude(user=request.user)
		p = Profile.objects.filter(slug=request.user.username).first()
		if p:
			sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
			rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
			friends = p.friends.all()
		
		Non_friend_user_list=[]
		if p:
			for user in users.all():
				if user not in request.user.profile.friends.all():
					Non_friend_user_list+=[user]

		if p:		
			args = {'users':Non_friend_user_list,
		        'friends_list': friends,
		        'sent_friend_requests': sent_friend_requests,
		        'rec_friend_requests': rec_friend_requests,
		        }
		else:
			args = {'users':Non_friend_user_list,
		         
		        }


		return render(request,self.template_name,args)		

	

	

