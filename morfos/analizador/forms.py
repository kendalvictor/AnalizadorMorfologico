from django import forms

class FormaEntrada(forms.Form):
    contenido = forms.CharField(widget=forms.Textarea)
