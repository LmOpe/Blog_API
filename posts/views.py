from rest_framework import generics

from posts.models import Post
from posts.permissions import IsAuthoOrReadOnly
from posts.serializers import PostSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthoOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthoOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer