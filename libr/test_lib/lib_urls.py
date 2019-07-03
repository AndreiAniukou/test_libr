from django.urls import path
from .views import *

urlpatterns = [
    path('', users_list, name='users_list_url'),
    path('users/<str:slug>/', UserDetail.as_view(), name='user_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
]