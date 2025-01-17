from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError

User = get_user_model()


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(
        min_length=7,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
            }
        ),
        label="Password",
    )

    password2 = forms.CharField(
        min_length=7,
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            }
        ),
        label="Password confirmation",
    )

    class Meta:
        model = User
        fields = ["username", "phone", "email"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2:
            try:
                password_validation.validate_password(password2, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_phone_number(self):
        phone = self.cleaned_data["phone"]
        if User.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("this phone number already exists")
        if not phone.isdigit():
            raise forms.ValidationError("phone must be a number.")
        if not phone.startswith("09"):
            raise forms.ValidationError("phone must start with 09 digits.")
        return phone


class UserChangeForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField(
    #     help_text='you can change password using <a href="../password/">this form</a>.'
    # )

    class Meta:
        model = User
        fields = ("email", "phone", "first_name", "last_name", "username")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
                }
            ),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone")
        if (
            User.objects.exclude(id=self.instance.id)
            .filter(phone_number=phone)
            .exists()
        ):
            raise forms.ValidationError("this phone number already exists")
        if not phone.isdigit():
            raise forms.ValidationError("phone must be a number.")
        if not phone.startswith("09"):
            raise forms.ValidationError("phone must start with 09 digits.")
        return phone

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError("this username already exists")
        return username
