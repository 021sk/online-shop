from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

User = get_user_model()


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(
        widget=forms.PasswordInput, label="password confirmation"
    )

    class Meta:
        model = User
        fields = ["username", "phone", "email", "password"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
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
        return phone


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='you can change password using <a href="../password/">this form</a>.'
    )

    class Meta:
        model = User
        fields = ("email", "phone", "first_name", "last_name", "password", "last_login")

    def clean_phone_number(self):
        phone = self.cleaned_data["phone"]
        if (
            User.objects.exclude(id=self.instance.id)
            .filter(phone_number=phone)
            .exists()
        ):
            raise forms.ValidationError("this phone number already exists")
        return phone

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError("this username already exists")
        return username
