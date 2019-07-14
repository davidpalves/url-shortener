from django.views.generic import ListView, CreateView, DetailView
from shorten.models import Encurtador
from shorten.forms import EncurtadorForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate


@method_decorator(login_required, name='dispatch')
class EncurtadorListView(ListView):
    model = Encurtador
    context_object_name = "urls"
    template_name = "home.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Encurtador.objects.filter(user=self.request.user)
        return queryset


@method_decorator(login_required, name='dispatch')
class EncurtadorCreateView(CreateView):
    model = Encurtador
    form_class = EncurtadorForm
    template_name = 'new_url.html'
    success_url = 'home'

    def form_valid(self, form):
        url = form.save(commit=False)
        url.user = self.request.user
        url.save()
        return redirect('home')


class EncurtadorDetailView(DetailView):
    model = Encurtador
    template_name = 'redirect.html'
    context_object_name = 'url'
    lookup_field = 'slug'


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
