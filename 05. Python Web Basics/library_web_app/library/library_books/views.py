from django.shortcuts import render, redirect

from library.library_books.forms import BookModelForm
from library.library_books.models import Book


# Create your views here.

def add_book(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BookModelForm()

    context = {
        "book_form": form,
    }
    return render(request, 'add-book.html', context=context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BookModelForm(instance=book)

    context = {
        'book': book,
        'edit_form': form
    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)
