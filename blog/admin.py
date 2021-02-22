from django.contrib import admin
from .models import Post, Comment, Comment_2_comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Comment_2_comment)
