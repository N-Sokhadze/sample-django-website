from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import ContactForm

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = ContactForm()
        # return render(request, 'contact.html')
    
    else:
        raise NotImplementedError
    return render(request, "contact.html", {'form': form})

    