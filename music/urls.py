from django.urls import path
from .views import IndexView, DetailView, AlbumCreate, AlbumUpdate, AlbumDelete

urlpatterns = [
    path('', IndexView.as_view(), name='music-index'),
    path('<int:pk>/', DetailView.as_view(), name='music-detail'),
    path('album/add/add/', AlbumCreate.as_view(), name='music-album-add'),
    path('album/<int:pk>/', AlbumUpdate.as_view(), name='music-album-update'),
    path('album/<int:pk>/delete/', AlbumDelete.as_view(),name='music-album-delete'),
    #path('<int:album_id>/favorite/', views.favorite, name='music-favorite')
]
