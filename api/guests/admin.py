from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models.user_auth_model import UserAuth


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = UserAuth
        fields = ["email",] #add all required fields

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
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserAuth
        fields = [
            "email", 
            "password", 
            "is_active", 
            ]   
        

class UserAdmin(BaseUserAdmin):
    # Forms para adicionar e alterar instâncias de usuário
    form = UserChangeForm
    add_form = UserCreationForm 

    # Os campos a serem usados ao exibir o modelo de User.
    list_display = ['id', 'email', 'is_staff', 'is_superuser', 'created_at']
    list_display_links = ['email']
    search_fields = ['email', 'username']
    list_filter = ['is_active', 'is_superuser', 'type_user', 'is_staff' ]
    list_per_page = 10  
    ordering = ['email']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('username', 'created_at')}),
        ('Datas Importantes', {'fields': ('last_login', )}),
    )

class GuestUserAdmin(admin.ModelAdmin):
    ... 

# Agora registre o novo UserAdmin...
admin.site.register(UserAuth, UserAdmin)