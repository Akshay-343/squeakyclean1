from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import AddressForm

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Address

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'index.html', )


def myaccount(request):
    return render(request, 'myaccount.html')


def services(request):
    return render(request, 'services.html', )


def contactus(request):
    return render(request, 'contact.html', )


def whoweare(request):
    return render(request, 'whoweare.html', )


def terms(request):
    return render(request, 'terms.html', )


@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted.')
        return redirect('signup')
    return render(request, 'delete_account.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['uemail']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        password = request.POST['passkey']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "Your account has been created successfully!")

        return render(request, 'registration/login.html')

    return render(request, 'registration/signup.html')


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressForm
    template_name ='address_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'address_list'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'address_update.html'
    success_url = reverse_lazy('address_list')


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'address_confirm_delete.html'
    success_url = reverse_lazy('address_list')


@login_required()
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'address_list.html', {'addresses': addresses})


@login_required()
def address_create(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        address = form.save(commit=False)  # create an unsaved Address object from the form data
        address.user = request.user  # set the user_id field to the current user
        address.save()  # save the Address object to the database
        return redirect('address_list')
    return render(request, 'address_form.html', {'form': form})


def address_update(request, pk):
    address = get_object_or_404(Address, pk=pk)
    form = AddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('address_list')
    return render(request, 'address_form.html', {'form': form})


def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'address_confirm_delete.html', {'address': address})
