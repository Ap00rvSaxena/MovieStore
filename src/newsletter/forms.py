from django import forms
from .models import SignUp


class ContactForm(forms.Form):
	email = forms.EmailField()
	full_name = forms.CharField()
	contact =  forms.IntegerField()
	message = forms.CharField()



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['first_name','email']