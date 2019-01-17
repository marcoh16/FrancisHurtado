from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def home(request):
	
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			
			form.save()
			try:
				send_mail(name, subject, message, ['practicepractice69@gmail.com'] ,)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "home.html" ,{'form': form})



def success(request):
	return HttpResponse('success my niggass')