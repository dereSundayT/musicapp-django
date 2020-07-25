from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='music-index'),
    path('<int:pk>/',views.detail,name='music-detail')
    path('<int:album_id>/favorite/',views.favorite,name='music-favorite')
]
