from django.views.generic import ListView, CreateView, DetailView, DeleteView
from shorten.models import Encurtador
from shorten.forms import EncurtadorForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.db.models import Q


@method_decorator(login_required, name='dispatch')
class EncurtadorListView(ListView):
    model = Encurtador
    context_object_name = "urls"
    template_name = "home.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Encurtador.objects.filter(
            user=self.request.user
            ).order_by('-id')

        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                (Q(url_redirect__icontains=search_query) |
                 Q(slug__icontains=search_query)) &
                Q(user=self.request.user)
                ).distinct()
        else:
            queryset = Encurtador.objects.filter(
                user=self.request.user
            ).order_by('-id')
        return queryset
        return queryset


@method_decorator(login_required, name='dispatch')
class EncurtadorCreateView(CreateView):
    model = Encurtador
    form_class = EncurtadorForm
    template_name = 'new_url.html'
    success_url = reverse_lazy('list_urls')

    def form_valid(self, form):
        url = form.save(commit=False)
        url.user = self.request.user
        url.save()
        return redirect('list_urls')


class EncurtadorDetailView(DetailView):
    model = Encurtador
    template_name = 'redirect.html'
    context_object_name = 'url'
    lookup_field = 'slug'


class EncurtadorDeleteView(DeleteView):
    model = Encurtador
    success_url = reverse_lazy('list_urls')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.request.user
        if self.object.user == user:
            return self.delete(request, *args, **kwargs)
        return redirect('url_list')


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
