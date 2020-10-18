from rest_framework import viewsets
from . import models
from . import serializers

class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer  # we have to use this serializer for post view set fro json conversion
#   this will create create(), delete(),retrieve(),update(),destroy()

class CommentViewset(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer  # we have to use this serializer for post view set fro json conversion
#   this will create create(), delete(),retrieve(),update(),destroy()

