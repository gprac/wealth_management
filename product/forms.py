from django import forms

from .models import Waterbill

class WaterbillForm(forms.ModelForm):
	class Meta:
		model = Waterbill
		fields = "__all__"
	def clean_volumes(self):
		volumes = self.cleaned_data.get('volumes')
		if volumes > 0:
			return volumes
		else :
			raise forms.ValidationError('数量非法')
