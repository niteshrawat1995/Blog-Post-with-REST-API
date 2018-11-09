from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.views.generic import CreateView
from django.urls import reverse_lazy




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save the user into the DB and hash the password.
            form.save()
            username = form.cleaned_data.get('username')
            # to show a flash message upon successfully creating a user.
            messages.success(request, f'Your account has been created! You can now log in with {username}!')
            # redirect user to the home page using urlpattern defined for blog's view.home
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class RegisterCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    success_message = "Congrats %(first_name)s! Your account has been created! You can now login with brand new %(username)s!"


@login_required
def profile(request):
    '''It's complex to handle 2 forms with classed based view so sticking to function based view.'''
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''
