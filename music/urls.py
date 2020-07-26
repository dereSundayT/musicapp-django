from django.urls import path
from .views import IndexView,DetailView
urlpatterns = [
    path('', IndexView.as_view(), name='music-index'),
    path('<int:pk>/', DetailView.as_view(), name='music-detail'),
   # path('<int:album_id>/favorite/', views.favorite, name='music-favorite')
]
