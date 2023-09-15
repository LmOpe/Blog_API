from django.urls import path
from rest_framework.routers import SimpleRouter

from posts.views import UserViewSet, PostViewSet

# urlpatterns = [
#     path("users/", UserList.as_view(), name="user_list"),
#     path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
# ]

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = router.urls