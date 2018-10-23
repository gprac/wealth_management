from django import forms

from .models import Waterbill

class WaterbillForm(forms.ModelForm):
	class Meta:
		model = Waterbill
		fields = "__all__"
