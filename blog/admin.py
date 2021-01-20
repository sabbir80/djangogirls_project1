from django.contrib import admin

from blog.models import Post
from blog.models import New_post


admin.site.register(Post)
admin.site.register(New_post)
