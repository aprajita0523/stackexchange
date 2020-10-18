from posts.viewset import PostViewset,CommentViewset

from rest_framework import routers

router = routers.DefaultRouter()
#now register router 
router.register('Post',PostViewset,)
router.register('Comment',CommentViewset,)

#map this to base url.py
#get,update , put ,delete  CommentViewset