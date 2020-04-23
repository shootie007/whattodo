from django.contrib.auth import forms as auth_forms


class SigninForm(auth_forms.AuthenticationForm):
    '''サインイン用のフォーム'''
    def init(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
