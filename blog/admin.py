from django.contrib import admin
from .models import Post, BlogComment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
        
admin.site.register(BlogComment)
