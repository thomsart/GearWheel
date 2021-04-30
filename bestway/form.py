from django import forms


class AddressForm(forms.Form):
    address_start = forms.CharField(label="Adresse de départ ", max_length=70)
    address_end = forms.CharField(label="Adresse d'arrivée ", max_length=70)