from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.decorators import login_required

from candidates.models import Candidato


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('rh:home')

        return render(request, 'login.html', {'error': 'incorrect username or password'})

    return render(request, 'login.html')


@login_required
def home_view(request):
    candidatos = Candidato.objects.all()
    return render(request, 'home.html', { 'candidatos': candidatos })
