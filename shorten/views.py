from django.views.generic import ListView, CreateView
from shorten.models import Encurtador
from shorten.forms import EncurtadorForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import redirect


@method_decorator(login_required, name='dispatch')
class EncurtadorListView(ListView):
    model = Encurtador
    context_object_name = "urls"
    template_name = "home.html"


@method_decorator(login_required, name='dispatch')
class EncurtadorCreateView(CreateView):
    model = Encurtador
    form_class = EncurtadorForm
    template_name = 'new_url.html'
    success_url = 'home'

    def form_valid(self, form):
        url = form.save(commit=False)
        url.user = User.objects.first()
        url.save()
        return redirect('home')
