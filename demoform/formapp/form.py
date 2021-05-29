from django import forms

class students(forms.Form):
	Roll_no=forms.IntegerField()
	Name=forms.CharField()