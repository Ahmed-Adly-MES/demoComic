
from django.urls import path

from myapp.views import *
urlpatterns = [ 
    path('', UserCreate.as_view() , name='user_create'),
    path('user/list', UserList.as_view() , name='user_list'),
    path('<pk>/details', UserDetails.as_view(),name = 'user_details'),
    path('<pk>/update', UserUpdate.as_view(),name = 'user_update'),
    path('<pk>/delete', UserDelete.as_view(),name = 'user_delete'),
    path('comic/create/<str:uid>', ComicCreate.create_view, name='comic_create'),
    path('comic/list', ComicList.as_view() , name='comic_list'),
]