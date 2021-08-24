from django import forms
from .models import Swiv


class SwivModelForm(forms.ModelForm):
	content = forms.CharField(label='' 
		,widget=forms.Textarea( 
			attrs={'placeholder':"your message", "class":"form-control"}))
	class Meta:
		model = Swiv  
		fields = [
			#"user",
			"content",
			
		]
		#exclude = ['user']


