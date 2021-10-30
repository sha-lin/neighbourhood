from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from estate.views import (BusinessDeleteView, 
                          BusinessListView,
                          BusinessCreateView,
                          BusinessDetailView,
                          BusinessUpdateView,
                          PostCreateView,
                          PostDeleteView,
                          PostDetailView,
                          PostUpdateView,
                          PostListView)


urlpatterns=[
    path('',BusinessListView.as_view(),name="home"),
    path('business/<int:pk>/',BusinessDetailView.as_view(),name='business-detail'),
    path('business/new/',BusinessCreateView.as_view(),name='business-create'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(),name='business-update'),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(),name='business-delete'),
    path('post/',PostListView.as_view(),name='post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.search_request,name='search_results'),
]