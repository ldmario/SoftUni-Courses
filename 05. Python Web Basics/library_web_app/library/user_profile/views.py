from django.shortcuts import render, redirect

from library.library_books.models import Book
from library.user_profile.forms import ProfileModelForm, DeleteProfileForm
from library.user_profile.models import Profile


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    if profile:
        template = 'home-with-profile.html'
    else:
        template = 'home-no-profile.html'
    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = ProfileModelForm()

    context = {
        'profile': profile,
        'profile_form': form,
        'books': books,
    }
    return render(request, template, context)


def profile_page(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        form.save()
        return redirect('profile_page')
    else:
        form = ProfileModelForm()

    context = {
        'edit_profile_form': form,
        'profile': profile
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    form = DeleteProfileForm(instance=profile)
    books = Book.objects.all()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            books.delete()
            return redirect('home_page')

    context = {
        'delete_profile_form': form,
        'profile': profile
    }

    return render(request, 'delete-profile.html', context)
