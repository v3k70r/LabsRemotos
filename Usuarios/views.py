from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

from .models import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import *

# paquete para modulo de usuarios
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

from .forms import EntradaForm
from django.shortcuts import redirect


# vista publica del sitiode
def vista_inicio(request):
    template_name = 'index.html'
    Entradas = Entrada.objects.all().order_by('-id')
    paginator = Paginator(Entradas, 3)
    page_number = request.GET.get('page')
    Entradas = paginator.get_page(page_number)
    banners = Banner.objects.all()
    return render(request, "index.html", {'entradas': Entradas, 'banners': banners})


# area privada del sitio, requiere login
def area_miembros(request):
    if request.user.is_authenticated:
        return render(request, "areaMiembros.html")
    return redirect('/login')


# Vistas genericas de django para sistema de usuarios
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "register.html", {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')


def entrada_new(request):
    form = EntradaForm()
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor = request.user
            entrada.save()
        return redirect('entrada_detail', pk=entrada.pk)
    else:
        form = EntradaForm()
    return render(request, 'entrada_edit.html', {'form': form})


def entrada_edit(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == "POST":
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.autor = request.user
            entrada.save()
            return redirect('entrada_detail', pk=entrada.pk)
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'entrada_edit.html', {'form': form})


def entrada_detail(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'entrada_detail.html', {'entrada': entrada})


def entrada_list(request):
    entradas = Entrada.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'entrada_list.html', {'entradas': entradas})


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
