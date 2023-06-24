from django import forms

from my_exam.myapp.models import Profile, Fruit


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['image_url', 'age']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Details'}),
        }


class DeleteFruitForm(FruitModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs = {'readonly': 'readonly'}


# class DeleteProfileForm(ProfileModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__set_disable_fields()
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.delete()
#
#     def __set_disable_fields(self):
#         for field in self.fields.values():
#             field.widget.attrs = {'readonly': 'readonly'}
#             field.widget.attrs = {'password': 'disabled'}


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['email', 'password']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'image_url': forms.URLInput(),
            'age': forms.NumberInput(),
        }
