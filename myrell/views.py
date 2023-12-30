from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login




def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def checkout(request):
    return render(request, 'checkout.html')


def pesan(request):
    return render(request, 'pesan.html')

def keranjang(request):
    return render(request, 'keranjang.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('beranda')
            else:
                form.add_error(None, "Username atau password salah.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
