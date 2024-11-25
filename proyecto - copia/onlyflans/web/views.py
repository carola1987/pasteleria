from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes_publicos': flanes_publicos})


def about(request):
    return render(request, 'about.html')


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados})


def contact_view(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactFormForm()
    return render(request, 'contactus.html', {'form': form})


def contact_success_view(request):
    return render(request, 'contact_success.html')
