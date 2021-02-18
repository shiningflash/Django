from django import forms

class InputForm(forms.Form):
    val1 = forms.EmailField()
    val2 = forms.CharField(max_length=255)
    