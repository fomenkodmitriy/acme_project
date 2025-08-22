from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayMixin:
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(BirthdayMixin, CreateView):
    pass


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayDeleteView(DeleteView):
    model = Birthday
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list') 


def birthday_delete(request, pk):
    instance = get_object_or_404(Birthday, pk=pk)
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    return render(request, 'birthday/birthday.html', context)
