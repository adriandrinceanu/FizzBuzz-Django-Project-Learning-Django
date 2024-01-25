from django import forms

class FizzbuzzForm(forms.Form):
    number = forms.IntegerField(label='Enter a number')
        