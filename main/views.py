from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return render(request, 'main/index.html')
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})