from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.



def home(request):
    """display homepage"""

    return render(request, 'home.html')



def contact_us(request):
    """display contact-us page"""

    # return Egytech contact info

    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.save
            return HttpResponseRedirect(reverse('landing_page:home'))

    context = { 'form' : form }
    return render(request, 'contact-us.html', context)
