from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from .forms import UserForm
from .models import Album, Song
from django.http import JsonResponse


class IndexView(ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'albums'
    # def get_queryset(self):
    #     return Album.objects.all()


class DetailView(DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music-index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # clean normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # return  User Objects  if credentaila are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music-index')
        return render(request, self.template_name, {'form': form})


def createSong(request, album_id):
    context = {'album': Album.objects.get(pk=album_id)}
    return render(request, 'music/create_song.html', context)


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


"""
def index(request):
    context = {'all_albums' : Album.objects.all()}
    return render(request,'music/index.html',context)

def detail(request,pk):
    album = get_object_or_404(Album,pk=pk)
    return render(request,'music/detail.html',{'album' : album})

def favorite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
         return render(request,'music/detail.html',{'album' : album, 'error_message':'You did not select a valid song'})
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album' : album})


def detail(request,pk):
    #album = Album.objects.filter(pk=pk).first()
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = {'album' : album}
    return render(request,'music/detail.html',context)
"""
