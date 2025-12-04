from django.urls import path
from ..views.user_views import UserListCreate, UserDetail

urlpatterns = [
    path("", UserListCreate.as_view(), name="user-list-create"),
    path("<str:_id>/", UserDetail.as_view(), name="user-detail"),
]
