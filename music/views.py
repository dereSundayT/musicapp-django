from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album


def index(request):
    context = {'all_albums' : Album.objects.all()}
    return render(request,'music/index.html',context)

def detail(request,pk):
    album = get_object_or_404(Album,pk=pk)
    return render(request,'music/detail.html',{'album' : album})
    
"""
def detail(request,pk):
    #album = Album.objects.filter(pk=pk).first()
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = {'album' : album}
    return render(request,'music/detail.html',context)
"""
