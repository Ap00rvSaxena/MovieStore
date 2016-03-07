from django.conf import settings

from django.core.mail import send_mail

from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	if request.user.is_authenticated():
		title="Welcome,%s"%(request.user)
	#form
	context = {
		"title" :title,
		"form" : form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		first_name = form.cleaned_data.get("first_name")
		if not first_name:
			first_name = "Empty"
		instance.first_name = first_name
		instance.save()
		context = {
		"title" : "YOu have Signed Up now"
		}

	return render (request,"home.html",context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print (key, form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_fullname = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		form_contact = form.cleaned_data.get("contact")

		context_message = "Email- %s\nFull Name-%s\nContact-%s\nMessage-%s\n"%(form_email, form_fullname,form_contact, form_message)
		fromemail = settings.EMAIL_HOST_USER
		tomail = [fromemail,'buzobuzz@gmail.com']

		send_mail('ContactForm', context_message, fromemail, tomail, fail_silently=False)

	context = {
	"form" : form,
	}
	return render (request, "contact.html",context)

