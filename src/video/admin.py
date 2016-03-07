from django.contrib import admin

# Register your models here.
from .forms import VideoForm
from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ["title","create_date","updated"]
	form = VideoForm

	search_fields = ["title", "content"]
	class Meta:
		model = Video

admin.site.register(Video, VideoAdmin)