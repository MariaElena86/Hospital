from django import forms

from management.models import Patient


class MatchForm(forms.Form):
    patient = forms.ModelChoiceField(Patient.objects.all(), required=True)


class SelectedForm(forms.Form):
    comment = forms.CharField(required=False)




