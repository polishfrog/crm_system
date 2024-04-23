from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

RATED = (
    (1, "Very Bad"),
    (2, "Bad"),
    (3, "Normal"),
    (4, "Good"),
    (5, "Best Ever"),
)


SEARCH_OPTION = (
    ("dateOpinion", "Date from height"),
    ("dateOpinion_reverse", "Date from low"),
    ("rated", "Rate from height"),
    ("rated_reverse", "Rate from low"),
)


class RatingForm(forms.Form):
    rated = forms.MultipleChoiceField(choices=RATED, required=False, label="Rated Opinion", widget=forms.CheckboxSelectMultiple)
    search_option = forms.ChoiceField(choices=SEARCH_OPTION, required=False, label="Filter:")
