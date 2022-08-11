from django.urls import path
from App1 import *
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.conf import settings




urlpatterns = [
    
    path('', index, name='index'),
    path('dash/', dash, name='dash'),
   # path('app1/dash', dash, name='dash'),
    path('about/', about, name='about'),
    
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', new_post, name='new_post'),
    path('post/<int:pk>edit/', edit_post, name= 'edit_post'),
    path('post/<int:pk>delete/', delete_post, name= 'delete_post'),
    
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('registerok/',register, name='registerok'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('user_detail/<pk>/', user_detail, name='user_detail'),
    path('user_profiles', user_profiles, name='user_profiles'),
    path('user_page/<pk>/', user_page.as_view(), name='user_page'),
    path('add_avatar/', add_avatar, name='add_avatar'),
    path('post1', posteo1, name= "Posteo1"),
    path('post2', posteo2, name= "Posteo2"),
    path('ups/', epaviejo,name="Ups"),
    path('chat',chat,name='chat'),
    path('chat/mandar_mensaje', MandarMensaje.as_view(), name='mandar_mensaje'),
]


