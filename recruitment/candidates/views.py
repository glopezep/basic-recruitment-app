from django.shortcuts import render

from .forms import CandidateForm


def new_view(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)

        return

    form = CandidateForm()
    context = { 'form': form }

    return render(request, 'new.html', context)
