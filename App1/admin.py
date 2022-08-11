from django.contrib import admin
from .models import Avatar, Post, MemberUser
# Register your models here.
admin.site.register(Post)
admin.site.register(MemberUser)
admin.site.register(Avatar)