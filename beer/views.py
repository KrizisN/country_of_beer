from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.base import View, TemplateResponseMixin

from .models import *

from .forms import AuthUserForm, CreateUserForm, ReviewForm


class SortMixin(TemplateResponseMixin):
    """Sugar for sort of beer"""
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sort_of_beer'] = Sort_of_beer.objects.all()
        return context


class LoginUserView(LoginView):
    """View for authentication users"""
    template_name = 'account/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')


class RegisterUserView(CreateView):
    """View for register users"""
    model = User
    template_name = 'account/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')


class BeerListView(SortMixin, ListView):
    """View for beer list display"""
    model = Beer
    queryset = Beer.objects.filter(is_available=True)
    template_name = 'beer/beer_list.html'
    context_object_name = 'beer_list'


class BeerDetailView(SortMixin, DetailView):
    """View for beer detail display"""
    model = Beer
    queryset = Beer.objects.all()
    template_name = 'beer/beer_detail.html'
    context_object_name = 'context_beer_detail'


class AddReviews(View):
    """View for do comments"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        beer = Beer.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.beer = beer
            form.user = request.user
            form.save()
            return redirect('home')
        else:
            return redirect('home')


class FilterBeer(SortMixin,ListView):
    def get_queryset(self):
        queryset = Beer.objects.filter(sort_of_beer__in=self.request.GET.getlist('sort_of_beer'))
        print(queryset)
        return queryset




