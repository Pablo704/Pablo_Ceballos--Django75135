from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field: '' for field in fields}
        
class MiFormularioDeEdicion(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False, label="Foto de perfil")
    biografia = forms.CharField(widget=forms.Textarea, required=False, label="Biografía")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label="Fecha de Nacimiento")
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','avatar', 'biografia', 'fecha_nacimiento']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['biografia'].initial = user.infoextra.biografia
            self.fields['fecha_nacimiento'].initial = user.infoextra.fecha_nacimiento
            self.fields['avatar'].initial = user.infoextra.avatar

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            info_extra = user.infoextra
            info_extra.biografia = self.cleaned_data.get('biografia')
            info_extra.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
            if self.cleaned_data.get('avatar'):
                info_extra.avatar = self.cleaned_data.get('avatar')
            info_extra.save()
        return user