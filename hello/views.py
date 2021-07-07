from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Greeting, Document

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('https://2chap.com/admin/dashboard')
    else:
        form = DocumentForm()
    return render(request, 'index.html', {
        'form': form,
    })


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
