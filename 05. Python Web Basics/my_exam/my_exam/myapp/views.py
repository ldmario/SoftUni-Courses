from django.shortcuts import render, redirect

from my_exam.myapp.forms import ProfileModelForm, FruitModelForm, DeleteFruitForm, DeleteProfileForm, \
    EditProfileModelForm
from my_exam.myapp.models import Profile, Fruit


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)


def dashboard(request):
    profile = Profile.objects.all()
    fruits = Fruit.objects.all()
    context = {
        'fruit': fruits,
        'profile': profile
    }
    return render(request, 'dashboard.html', context)


def fruit_create(request):
    profile = Profile.objects.all()
    fruits = Fruit.objects.all()

    if request.method == 'POST':
        form = FruitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = FruitModelForm()
    context = {
        'create_fruit_form': form,
        'profile': profile,
        'fruit': fruits
    }
    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': fruit,
    }
    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):
    profile = Profile.objects.all()
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        form = FruitModelForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitModelForm(instance=fruit)
    context = {
        'edit_fruit_form': form,
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):
    profile = Profile.objects.all()
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteFruitForm(instance=fruit)
    context = {
        'delete_fruit_form': form,
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'delete-fruit.html', context)


def profile_create(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = ProfileModelForm()
    context = {
        'create_profile_form': form,
        'profile': profile
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    fruit = Fruit.objects.all()
    number_posts = len(fruit)
    context = {
        'profile': profile,
        'posts': number_posts,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileModelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditProfileModelForm(instance=profile)
    context = {
        'edit_profile_form': form,
        'profile': profile
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Fruit.objects.all().delete()
        return redirect('home_page')

    return render(request, 'delete-profile.html')
