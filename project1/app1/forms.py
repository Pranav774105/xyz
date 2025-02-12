from django import forms

class StudentForm(forms.Form):
    roll = forms.IntegerField()
    name = forms.CharField(max_length=80)
    marks = forms.FloatField()
