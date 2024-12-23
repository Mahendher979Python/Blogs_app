from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.template.context_processors import request

# User Registration View
def user_reg(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect("posts:list")
        else:
            print(form.errors)  # Log errors for debugging
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

# User Login View
def user_log(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get("next")  # Handle the 'next' parameter for redirects
            return redirect(next_url) if next_url else redirect("posts:list")
        else:
            print(form.errors)  # Log errors for debugging
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

# User Logout View
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")
    else:
        # Optionally, allow GET requests for logout
        logout(request)
        return redirect("posts:list")

#Logout
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")
    return HttpResponseNotAllowed(["POST"])  # Respond with 405 Method Not Allowed for other methods

