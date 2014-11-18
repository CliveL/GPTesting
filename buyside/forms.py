__author__ = 'Clive'
from django import forms

class VehicleDetailForm(forms.Form):
    FUEL_CHOICES = (
        (0, ""),
        (1, "Petrol"),
        (2, "Diesel"),
        (3, "Electric")
    )
    make = forms.CharField(label="Make")
    model = forms.CharField(label="Model")
    year = forms.DecimalField(max_digits=4, decimal_places=0, label="Year of Manufacture")
    #engine = forms.CharField(label="Engine Size")
    #transmission = forms.ChoiceField(label="Transmission Type")
    fuel = forms.ChoiceField(label="Fuel Type", choices=FUEL_CHOICES)
    #bodytype = forms.CharField(label="Body Type")