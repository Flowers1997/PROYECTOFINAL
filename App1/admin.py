from django.contrib import admin
from .models import Avatar, Mensaje, Post, MemberUser
# Register your models here.
admin.site.register(Post)
admin.site.register(MemberUser)
admin.site.register(Avatar)
admin.site.register(Mensaje)