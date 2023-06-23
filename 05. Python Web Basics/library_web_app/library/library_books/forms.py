from django import forms

from library.library_books.models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'image': forms.URLInput(),
            'type': forms.TextInput(),
        }