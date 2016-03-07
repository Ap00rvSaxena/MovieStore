from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "first_name","last_name" ,"timestamp","updated"]
	# list_display = ["__str__", "first_name","last_name" ,"timestamp"]

	# class Meta:
	# 	model = SignUp
	form = SignUpForm

		

admin.site.register(SignUp, SignUpAdmin)
