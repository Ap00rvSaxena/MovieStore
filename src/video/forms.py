from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		# fields = ['title','desc','slug']
		fields = ['title','desc','movie','image']