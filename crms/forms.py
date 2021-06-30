from django import forms
from django.db.models import fields
from .models import Criminal, FIR, Victim, Writer

class WriterForm(forms.ModelForm):
    class Meta:
        model=Writer
        fields='__all__'

class CriminalForm(forms.ModelForm):
    class Meta:
        model=Criminal
        fields='__all__'

class VictimForm(forms.ModelForm):
    class Meta:
        model=Victim
        fields='__all__'

class FIRForm(forms.ModelForm):
    class Meta:
        model=FIR
        fields='__all__'
