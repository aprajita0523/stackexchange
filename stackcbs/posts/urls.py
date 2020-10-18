from django.urls import path 

from .views import post_comment_create_and_list_view,like_unlike_post,PostDeleteView,PostUpdateView

app_name = 'posts'  #important

urlpatterns = [
    path('',post_comment_create_and_list_view, name='main-post-view'),#used in view for redirect
    path('liked/',like_unlike_post, name='like-post-view'), #use this name in main.html
    path('<pk>/delete/',PostDeleteView.as_view(), name='post-delete'), #this path expect the primary key , set in views
    path('<pk>/update/',PostUpdateView.as_view(), name='post-update'), #this path expect the primary key , set in views


]


#http://127.0.0.1:8000/profiles -- will already be defined in main.urls.py