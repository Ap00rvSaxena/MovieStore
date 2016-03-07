from .forms import VideoForm
from .models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import VideoForm
from django.contrib import messages
# Create your views here

def video_list(request):
	form = VideoForm(request.POST or None)
	title = "All Videos"
	today = timezone.now().date()
		# print(SignUp.objects.all())
		# for instance in SignUp.objects.all():
		# 	print (instance.full_name)
	queryset_list = Video.objects.all().order_by("-create_date")#.filter(full_name__iexact="Buzo")

	paginator = Paginator(queryset_list, 4)
	
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"title" :title,
		"queryset" : queryset,
		"today" : today
		}


	return render(request,"videolist.html",context)

def video_play(request,slug=None):
	instance = get_object_or_404(Video,slug=slug)
	# title = "Playing:-%s"%instance.title
		# print(SignUp.objects.all())
		# for instance in SignUp.objects.all():
		# 	print (instance.full_name)

	context = {
		"title" :"Playing:-%s"%instance.title,
		"videoid" : "%s.mp4"%instance.id,
		"instance" : instance,
		}


	return render(request,"videobasic.html",context)

def video_upload(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	title = "Upload Your Video"
	button = "upload"
	form =  VideoForm(request.POST or None, request.FILES or None, request.FILES or None)
	context = {
		"title" :title,
		"form" : form,
		"button" : button,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	return render(request,"video_form.html",context)

def video_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	button = "update"
	instance = get_object_or_404(Video, slug=slug)
	form = VideoForm(request.POST or None, request.FILES or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='list'>Video</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
		"button" :button,
	}
	return render(request, "video_form.html", context)

def video_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Video, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("list")