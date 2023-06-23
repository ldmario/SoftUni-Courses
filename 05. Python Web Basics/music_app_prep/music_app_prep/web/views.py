from .models import Profile, Album
from .forms import ProfileModelForm, AlbumModelForm, DeleteAlbumModelForm

from django.shortcuts import render, redirect


def index(request):
    profile = Profile.objects.first()
    albums = Album.objects.all().order_by('id')

    if not profile:
        template = 'web/home-no-profile.html'
    else:
        template = 'web/home-with-profile.html'

    if request.method == "GET":
        form = ProfileModelForm()
    else:
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
        'albums': albums,
    }

    return render(request, template_name=template, context=context)


def add_album(request):
    if request.method == "GET":
        form = AlbumModelForm()
    else:
        form = AlbumModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }
    return render(request, template_name='web/add-album.html', context=context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, template_name='web/album-details.html', context=context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == "GET":
        form = AlbumModelForm(instance=album)
    else:
        form = AlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, template_name='web/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = DeleteAlbumModelForm(instance=album)

    if request.method == "POST":
        form = DeleteAlbumModelForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'delete_form': form,
        'album': album,
    }
    return render(request, template_name='web/delete-album.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    albums = len(Album.objects.all())
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, template_name='web/profile-details.html', context=context)


def delete_profile(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Album.objects.all().delete()
        return redirect('home page')

    return render(request, template_name='web/profile-delete.html')
