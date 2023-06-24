from string import ascii_lowercase, ascii_uppercase

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class StartWithLetter():
    def __call__(self, username):
        def __call__(self, name):
            if len(name) > 0:
                x = name[0]
                if not x.isalpha():
                    raise ValidationError("Your name must start with a letter!")

    def __eq__(self, other):
        return True


@deconstructible()
class NameOnlyLetters:
    def __call__(self, name):
        for y in name:
            if not y.isalpha():
                raise ValidationError("Fruit name should contain only letters!")

    def __eq__(self, other):
        return True
