from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import Client

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    # username = forms.CharField(
    #     label = 'Имя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   'class': 'form-control',
    #                                   'placeholder': 'Введите ваше имя пользователя'})
    # )
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'form-control',
    #                                       'placeholder': 'Введите ваш пароль'})
    # )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите вашу фамилию",
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя пользователя",
    #         }
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваш email *youremail@example.com",
    #         }
    #     )
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваш пароль",
    #         }
    #     )
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Поддтвердите ваш пароль",
    #         }
    #     )
    # )


from django.contrib.auth.hashers import make_password, check_password


class ProfileForm(UserChangeForm):
    class Meta:
        model = Client
        fields = ("image", "first_name", "last_name", "username", "email", "password")

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # If the form is bound to an instance, decrypt the password to show it in the form
        if self.instance and self.instance.pk:
            self.fields['password'].initial = self.instance.password  # Assign encrypted password to the field

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            # Re-encrypt the password before saving
            return make_password(password)
        return self.instance.password  # If password is not provided, use the current password

# class ProfileForm(UserChangeForm):
#     class Meta:
#         model = Client
#         fields = (
#             "image",
#             "first_name",
#             "last_name",
#             "username",
#             "email",
#             "password")
#
#     image = forms.ImageField(required=False)
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     username = forms.CharField()
#     email = forms.CharField()
#     password = forms.CharField()

# image = forms.ImageField(
#     widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
# )
# first_name = forms.CharField(
#     widget=forms.TextInput(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Введите ваше имя",
#         }
#     )
# )
# last_name = forms.CharField(
#     widget=forms.TextInput(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Введите вашу фамилию",
#         }
#     )
# )
# username = forms.CharField(
#     widget=forms.TextInput(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Введите ваше имя пользователя",
#         }
#     )
# )
# email = forms.CharField(
#     widget=forms.EmailInput(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Введите ваш email *youremail@example.com",
#             # 'readonly': True,
#         }
#     ),
# )
