from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import ExamUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = ExamUser
        fields = ('login', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'


class RegisterForm(UserCreationForm):
    class Meta:
        model = ExamUser
        fields = ('name', 'surname', 'patronymic', 'login', 'password1', 'password2', 'rules')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''
