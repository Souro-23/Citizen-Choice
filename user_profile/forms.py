from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()


	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)

		for fieldname in ['username','email', 'password1', 'password2' ]:
			self.fields[fieldname].help_text = None
			self.fields[fieldname].label =False
			self.fields[fieldname].widget.attrs.update({'placeholder': 'Search','class':'btn-primary'})


			#print(self.fields[fieldname].attrs)