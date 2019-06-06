from django.contrib import admin
from .models import Post
# Register your models here.
#admin.site.register(Post)
admin.site.site_header = '디지털이펙트 admin'
admin.site.site_title = '디지털이펙트 admin'
#admin.site.site_url = 'http:///'
admin.site.index_title = '디지털이펙트 administration'
admin.empty_value_display = '**Empty**'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
#    list_display=['id','title','auth','created-date']
     list_display=['id','title','is_public','created_date'] 
     list_display_links=['title'] 
     # list_editable=['is_public']

