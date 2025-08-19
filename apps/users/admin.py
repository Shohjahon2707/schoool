from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from apps.users.models import User


class UserCreationForm(forms.ModelForm):
    """Форма для создания новых пользователей с username и паролем."""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username"]  # только username при создании

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


class UserChangeForm(forms.ModelForm):
    """Форма для обновления пользователей — все поля и хеш пароля."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"  # показать все поля


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "email", "phone_number"]
    search_fields = ["username", "email", "phone_number"]
    ordering = ["username"]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": (
            "first_name", "last_name", "email", "date_of_birth", "gender", "phone_number",
            "address", "bio", "pfp", "qr_code"
        )}),
        ("Preferences", {"fields": ("shift", "study_lang", "blood_group", "teacher_rating")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
        "shift",
        "study_lang",
        "blood_group",
        "gender",
    ]

    fieldsets = [
        (None, {"fields": ["email", "username", "password"]}),
        ("Personal info", {
            "fields": [
                "first_name", "last_name", "date_of_birth", "phone_number", "address",
                "shift", "study_lang", "blood_group", "gender", "teacher_rating", "qr_code", "pfp", "bio"
            ]
        }),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2", "shift", "study_lang"],
            },
        ),
    ]


# Регистрация модели
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
