from django import forms
from .models import AirportRoute


class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ["airport_code", "position", "duration", "left", "right"]
        widgets = {
            "airport_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g., JFK, LAX, DEL"}
            ),
            "position": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g., Main Hub, Regional Terminal, International Gateway",
                }
            ),
            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Duration in minutes",
                    "min": "0",
                }
            ),
            "left": forms.Select(attrs={"class": "form-control"}),
            "right": forms.Select(attrs={"class": "form-control"}),
        }
        help_texts = {
            "airport_code": "Unique airport identifier (e.g., JFK, LAX)",
            "position": "Position in the route network",
            "duration": "Flight duration in minutes",
            "left": "Select left child airport (optional)",
            "right": "Select right child airport (optional)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["left"].queryset = AirportRoute.objects.exclude(
                pk=self.instance.pk
            )
            self.fields["right"].queryset = AirportRoute.objects.exclude(
                pk=self.instance.pk
            )
        self.fields["left"].required = False
        self.fields["right"].required = False


class SearchLastReachableNodeForm(forms.Form):
    DIRECTION_CHOICES = [
        ("left", "Left"),
        ("right", "Right"),
    ]

    airport = forms.ModelChoiceField(
        queryset=AirportRoute.objects.all().order_by("airport_code"),
        empty_label="Select an airport",
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Select the starting airport node",
    )

    direction = forms.ChoiceField(
        choices=DIRECTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        help_text="Choose the direction to traverse",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["airport"].queryset = AirportRoute.objects.all().order_by(
            "airport_code"
        )
