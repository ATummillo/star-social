from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.PostList.as_view(),
        name='all'),
    path(
        'new/',
        views.CreatePost.as_view(),
        name='create'),
    path(
        'by/<username:username>/',
        views.PostList.as_view(),
        name='for_user'),
    path('delete/<pk:pk>/', views.DeletePost.as_view(), name='delete')
]
