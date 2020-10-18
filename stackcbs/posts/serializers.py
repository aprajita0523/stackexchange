from rest_framework import serializers
from .models import Post,Comment,Like

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content',)  # to use all fields '__all__' can be used 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body',)   

#first reate serialisers then view sets the router.py and then map to urls             
