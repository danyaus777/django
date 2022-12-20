from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from requests import delete
from .forms import UserRegisterForm, CreateForm
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse

User = get_user_model()


def index(request):
    tickets_main = DesignForm.objects.filter(status=3).order_by('-created_date')[:4]
    count = DesignForm.objects.filter(status=2).count()
    context = {
        'tickets_main': tickets_main,
        'count': count
    }
    return render(request, 'index.html', context)


def about(request):
    template_name = 'about.html'
    return render(request, template_name)


@login_required
def profile(request):
    tickets = DesignForm.objects.filter(user=request.user).order_by('-created_date')
    template_name = 'profile.html'
    return render(request, template_name, {'tickets': tickets})


@login_required
def profile_work(request):
    tickets = DesignForm.objects.filter(user=request.user, status=2 ).order_by('-created_date')
    template_name = 'profile_work.html'
    return render(request, template_name, {'tickets': tickets})


@login_required
def profile_new(request):
    tickets = DesignForm.objects.filter(user=request.user, status=1 ).order_by('-created_date')
    template_name = 'profile_new.html'
    return render(request, template_name, {'tickets': tickets})


@login_required
def profile_done(request):
    tickets = DesignForm.objects.filter(user=request.user, status=3 ).order_by('-created_date')
    template_name = 'profile_done.html'
    return render(request, template_name, {'tickets': tickets})


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким логином уже зарегестрирован')
        else:
            if form.is_valid():
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                fio = form.cleaned_data['fio']

                user = authenticate(username=username, password=password, email=email, )
                ins.email = email
                ins.fio = fio
                ins.save()
                form.save(commit=False)
                form.save_m2m()
                messages.success(request, 'Вы успешно зарегестрировались')
                return redirect('/')


    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Вы успешно создали заявку')
            return redirect('profile')
    else:
        form = CreateForm()
    return render(request, 'create.html', {'form': form})


@login_required
def delete(request, pk):
    act = get_object_or_404(DesignForm, pk=pk, status=1)
    if not request.user.is_author(act):
        return redirect('profile')
    if request.method == 'POST':
        act.delete()
        return redirect('profile')
    else:
        context = {'act': act}
    return render(request, 'profile_delete.html', context)

