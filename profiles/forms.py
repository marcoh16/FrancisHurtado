from django import forms
from django.forms import ModelForm
from .models import Contact
from crispy_forms.helper import FormHelper

class ContactForm(forms.ModelForm):


	
	class Meta:
		model = Contact
		fields = ('name', 'email', 'subject', 'message',)


		widgets = {
			'name': forms.TextInput(attrs={'placeholder':'Name'}),
			'email': forms.TextInput(attrs={'placeholder':'Email'}),
			'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
			'message': forms.TextInput(attrs={'placeholder': 'Message'}),
		}

		


