from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import GuestForm
from webapp.models import Guest


def add_guest(request: WSGIRequest):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'guest_add.html', context={'form': form})

    form = GuestForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'guest_add.html', context={'form': form})
    else:
        guest = Guest.objects.create(**form.cleaned_data)
        return redirect(f'/', pk=guest.pk)


def update_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)

    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'guest_update.html', context={'form': form, 'guest': guest})

    form = GuestForm(instance=guest)
    return render(request, 'guest_update.html', context={'form': form, 'guest': guest})


def delete_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)

    if request.method == 'GET':

        return render(request, 'guest_delete.html', context={'guest': guest})

    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
