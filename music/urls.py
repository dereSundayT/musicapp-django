from django.urls import path
from .views import IndexView, DetailView, AlbumCreate, AlbumUpdate, AlbumDelete, UserFormView, createSong, favorite_album

urlpatterns = [
    path('', IndexView.as_view(), name='music-index'),
    path('register/', UserFormView.as_view(), name='music-register'),
    
    path('<int:pk>/', DetailView.as_view(), name='music-detail'),
    path('album/add/add/', AlbumCreate.as_view(), name='music-album-add'),
    path('album/<int:pk>/', AlbumUpdate.as_view(), name='music-album-update'),
    path('album/<int:pk>/delete/', AlbumDelete.as_view(),
         name='music-album-delete'),
    path('<int:album_id>/create_song/', createSong, name="music-create-song"),
    path('<int:album_id>/favorite/', favorite_album, name='music-favorite-album'),
]
