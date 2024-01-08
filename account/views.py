from django.shortcuts import render, redirect

from .forms import RegistrationForm


def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('store')

    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)
