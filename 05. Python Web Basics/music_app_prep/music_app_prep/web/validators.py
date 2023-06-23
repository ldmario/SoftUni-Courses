from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CharAndUnderscoreValidator:
    def __call__(self, username):
        for char in username:
            if not char.isalnum() and not char == '_':
                raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

    def __eq__(self, other):
        return True
