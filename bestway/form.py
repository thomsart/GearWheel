from django import forms


class AddressForm(forms.Form):
    start = forms.CharField(label="Adresse de départ ", max_length=70)
    end = forms.CharField(label="Adresse d'arrivée ", max_length=70)