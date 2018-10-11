from django.shortcuts import render, redirect

from .models import Candidato

from human_resources.models import Puesto

from .forms import CandidateForm, ExperienciaForm

def new_view(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)

        if (form.is_valid()):
            form.save()
        else:
            form = CandidateForm(request.POST)
            context = { 'form': form, 'error': 'Cedula invalida'}
            return render(request, 'new.html', context)

        return redirect('home')

    form = CandidateForm()
    context = { 'form': form }

    return render(request, 'new.html', context)


def new_experience_view(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)

        if (form.is_valid()):
            form.save()
        else:
            form = ExperienciaForm(request.POST)
            return render(request, 'new_experience.html', {})

    form = ExperienciaForm()
    context = { 'form': form }

    return render(request, 'new_experience.html', context)


def login_view(request):
    if request.method == 'POST':
        cedula = request.POST['cedula']
        return redirect(f'/candidates/detail/{cedula}')

    return render(request, 'candidates_login.html', {})


def detail_view(request, cedula):        
    if request.method == 'POST':
        try:
            candidato = Candidato.objects.get(cedula=request.POST['cedula'])

            form = CandidateForm(request.POST, instance=candidato)

            form.save()

            return render(request, 'candidates_detail.html', { 'candidato': candidato, 'form': form })

        except Candidato.DoesNotExist:
            return redirect('candidates:login')    

    
    try:
        candidato = Candidato.objects.get(cedula=cedula)
    except Candidato.DoesNotExist:
        return redirect('candidates:login')    

    form = CandidateForm(instance=candidato)

    return render(request, 'candidates_detail.html', { 'candidato': candidato, 'form': form })