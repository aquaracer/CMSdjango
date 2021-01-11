from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(label='Ваше имя', required=True)
    email = forms.EmailField(label='Электронная почта', required=True)
