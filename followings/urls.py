from django.urls import path
from .views import FollowingView

urlpatterns = [
    path("books/followings/", FollowingView.as_view()),
]
