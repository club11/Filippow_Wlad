from django import forms

class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label='Контактные данные*', required=True, widget=forms.TextInput())
    tel = forms.CharField(label='тел.')
