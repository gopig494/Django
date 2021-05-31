from django import forms
from IT_Team.models import empdetails


class form(forms.ModelForm):
	class meta:
		model=empdetails 
		fields='__all__'
		