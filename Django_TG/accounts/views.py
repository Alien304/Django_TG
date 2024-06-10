from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from .forms import UserEditForm

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            update_session_auth_hash(request, user_form.instance)  # Update session with new password hash
            password_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'password_form': password_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page or render a different template
        else:
            # Return an error message or render the login form again with an error
            pass
    else:
        # Render the login form
        return render(request, 'accounts/login.html')
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to a success page or render a different template
            return redirect('home')  # Replace 'home' with the name of your home page URL pattern
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')