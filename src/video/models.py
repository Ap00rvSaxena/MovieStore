from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    VideoModel = instance.__class__
    new_id = VideoModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)



class Video(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField(max_length=2000)
	slug = models.SlugField(unique=True)
	movie = models.FileField(upload_to=upload_location, null=True, blank=True)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("play", kwargs={"slug": self.slug})
	class Meta:
		ordering = ["-create_date","-updated"]


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Video.objects.filter(slug=slug).order_by("-id")
	exists =  qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_video_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_video_receiver, sender=Video)

