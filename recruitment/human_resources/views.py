from django.shortcuts import render, redirect

from django.http import HttpResponse, FileResponse

from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from candidates.models import Candidato

from .models import Empleado

from io import BytesIO

from django.template.loader import get_template

import xhtml2pdf.pisa as pisa

from django.views.generic import View

from django.utils import timezone

class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            http_response = HttpResponse(response.getvalue(), content_type='application/pdf')
            http_response['Content-Disposition'] = 'attachment;filename=report_file.pdf'
            return http_response
        else:
            return HttpResponse("Error Rendering PDF", status=400)



class Pdf(View):

    def get(self, request):
        candidatos = Candidato.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'candidatos': candidatos,
            'request': request,
            'is_report': True
        }
    
        return Render.render('report.html', params)

        

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
def logout_view(request):
    logout(request)
    return redirect('rh:login')


@login_required
def home_view(request):
    candidatos = Candidato.objects.all()
    return render(request, 'home.html', { 'candidatos': candidatos })


@login_required
def reclutar_view(request, id):
    candidato = Candidato.objects.get(pk=id)

    candidato.esta_reclutado = True

    candidato.save()
    
    user = User.objects.create_user(
        username=candidato.cedula,
        password=candidato.cedula,
    )

    Empleado.objects.create(
        user=user,
        cedula=candidato.cedula,
        nombre=candidato.nombre,
        departamento=candidato.departamento
    )


    return redirect('rh:home')
