from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you are now logged in.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render (request, 'users/register.html', {'form':form})


# login_required() does the following: - If the user isn’t logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Example: /accounts/login/?next=/polls/3/. If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.
@login_required
def profilepage(request):
    return render(request, 'users/profile.html')