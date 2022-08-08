from django.urls import path
from App1 import *
from .views import *
#USER SISTEM
from django.contrib.auth.views import LogoutView




urlpatterns = [
    #BLOG
    path('', index, name='index'),
    path('dash/', dash, name='dash'),
   # path('app1/dash', dash, name='dash'),
    path('about/', about, name='about'),
    #CRUD
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', new_post, name='new_post'),
    path('post/<int:pk>edit/', edit_post, name= 'edit_post'),
    path('post/<int:pk>delete/', delete_post, name= 'delete_post'),
    #USER SISTEM
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('registerok/',register, name='registerok'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('user_detail/<pk>/', user_detail, name='user_detail'),
    path('user_profiles', user_profiles, name='user_profiles'),
    path('user_page/<pk>/', user_page.as_view(), name='user_page'),
    path('add_avatar/', add_avatar, name='add_avatar'),
]


