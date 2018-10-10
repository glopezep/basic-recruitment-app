from django.shortcuts import render

from .forms import CandidateForm


def new_view(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)

        if (form.is_valid()):
            form.save()
        else:
            print(form)

        return

    form = CandidateForm()
    context = { 'form': form }

    return render(request, 'new.html', context)
