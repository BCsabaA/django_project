from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
# 1. step def
# 2. register.html
# 4. step create forms.py and set custom fields for the form
# 5. step install crispy and edit in settings: INSTALLED_APPS and CRISPY_TEMPLATE_PACK(at the very end of the settings file)
# 6. step load crispy in register.html
# 7. step register.html: change form.as_p() to form|crispy -> {{ form|crispy }} <- (filter crispy)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})