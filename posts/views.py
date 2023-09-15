from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from posts.models import Post
from posts.permissions import IsAuthoOrReadOnly
from posts.serializers import PostSerializer, UserSerializer

# Create your views here.

# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthoOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthoOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthoOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer