from django.contrib import admin
from  .models import  Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_display = [
    'title',
    'description',
    'created_at', 
    'created_by',
    'thumbnail' 
]
admin.site.register(Posts, PostAdmin)