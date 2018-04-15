from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

#iitg backend
from iitgauth.views import WebmailLoginView
from django.urls import reverse_lazy

from bookingportal.forms import SignUpForm




class IndexTemplateView(TemplateView):
    template_name = 'bookingportal/index.html'


class CalendarListView(LoginRequiredMixin, ListView):
    template_name = 'bookingportal/calendar.html'
    model = Entry
    context_object_name = 'entries'

    def get_queryset(self, *args, **kwargs):
        return Entry.objects.filter(author=self.request.user)


class EntryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'bookingportal/details.html'
    model = Entry
    context_object_name = 'entry'

# CreateView

# DeleteView


@login_required
def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            field_name = form.cleaned_data['field_name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            slot = form.cleaned_data['slot']

            Entry.objects.create(
                field_name=field_name,
                author=request.user,
                date=date,
                slot=slot,
                description=description,
            ).save()

            return HttpResponseRedirect('/calendar')

    else:
        form = EntryForm()

    return render(request, 'bookingportal/form.html', {'form': form})

@login_required
def delete(request, pk):

    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')


#login iitg auth
class LoginView(WebmailLoginView):
    """
    View class which handles logging in users. It is subclass of
    ``WebmailLoginView`` class provided by ``iitgauth`` package.
    """
    template_name = 'registration/login.html'
    success_url = reverse_lazy('calendar')

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.profile.first_name = form.cleaned_data['first_name']
            user.profile.last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user.profile.roll_number = form.cleaned_data['roll_number']
            user.profile.branch = form.cleaned_data['branch']
            user.profile.year = form.cleaned_data['year']

            user.profile.course = form.cleaned_data['course']
            user.save()
            raw_password = form.cleaned_data.get('password1')

            user1 = authenticate(username=username, password=raw_password)
            login(request, user1)
            return redirect('/calendar')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
