>>> from music.models import Album,Song
>>> Album.objects.all()
<QuerySet []>
>>> a = Album(artist='Dere ', album_title='red', genre="Country", album_logo='img.jpg')
>>> a
<Album: Album object (None)>
>>> a.save()
>>> a.artist
'Dere '
>>> Album.objects.all()
<QuerySet [<Album: Album object (1)>]>
>>> a.id
1
>>> a.pk
1
>>> b = Album()
>>> b.artist="dara"
>>> b.album_title = "Hello From the other sider"
>>> b.genre= "Punk"
>>> b.album_logo = "img.jpg"
>>> b.save()
>>> b.album_logo = "img_1.jpg"
>>> b.save()
>>> b.album_logo
'img_1.jpg'
>>> Album.objects.all()
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>
>>>
>>> from music.models import Album,Song
>>> Album.objects.all()
<QuerySet [<Album: red-Dere >, <Album: Hello From the other sider-dara>]>
>>> Album.objects.filter(id=1)
<QuerySet [<Album: red-Dere >]>
>>> Album.objects.filter(pk=1)
<QuerySet [<Album: red-Dere >]>
>>> Album.objects.filter(artist__startswith='dere')
<QuerySet [<Album: red-Dere >]>
>>>
>>> from music.models import Album,Song
>>> album1 = Album.objects.get(pk=1)
>>> album1.album_title
'red'
>>> song = Song()
>>> song = album1
>>> song = Song()
>>> song.album = album1
>>> song.file_type = 'mp3'
>>> song.song_title = 'Jesus saves'
>>> song.save()
>>> album1.song_set.all()
<QuerySet [<Song: Jesus saves>]>
>>> album1.song_set.create(file_type="mp4",song_title="God is good")
<Song: God is good>
>>> album1.song_set.all()
<QuerySet [<Song: Jesus saves>, <Song: God is good>]>
>>> album1.song_set.create(file_type="mp4",song_title="God is good to me")
<Song: God is good to me>
>>> song = album1.song_set.create(file_type="mp4",song_title="God is good to me")
>>> song
<Song: God is good to me>
>>> song.album
<Album: red-Dere >
>>> song.album.album_title
'red'
>>> album1.song_set.all()
<QuerySet [<Song: Jesus saves>, <Song: God is good>, <Song: God is good to me>, <Song: God is good to me>]>
>>> album1.song_set.count()
4
>>>