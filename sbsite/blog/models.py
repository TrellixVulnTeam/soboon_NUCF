from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.fields import RichTextField
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, null=True)
    #content = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    content2 = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[(
                                          'youtube',
                                          '/static/vendor/ckeditor_plugins/youtube/youtube/',
                                          'plugin.js',
                                          )],
        )
     # photo = models.ImageField( null=True)
    is_public = models.BooleanField(default=False)
#    새로운 필드 추가 첫째 makemigrations App 둘째 migrate App
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id]) 

class Images(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
		

	def __str__(self):
		return self.post.title + "Image"
        # return self.post.title + "Image"
