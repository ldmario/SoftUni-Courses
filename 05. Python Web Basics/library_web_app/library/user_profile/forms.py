from django import forms

from library.user_profile.models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'image_url': forms.URLInput()
        }


class DeleteProfileForm(ProfileModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_fields_false()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_fields_false(self):
        for field in self.fields.values():
            field.widget.attrs = {'readonly': 'readonly'}
