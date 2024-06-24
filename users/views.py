from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm


def create_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                user.set_password(password1)
                user.save()
                return redirect('login')
    context = {
        "form": CustomUserCreationForm
    }
    return render(request, "signup.html", context=context)
