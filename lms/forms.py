from django.contrib.auth.forms import UserCreationForm
from lms.models import User  # Import your custom User model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use the custom User model
        fields = (
            "username",
            "email",
            "display_name",
            "full_name",
            "password1",
            "password2",
        )
