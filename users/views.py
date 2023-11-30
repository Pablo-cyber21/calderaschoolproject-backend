from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_user(request):
    """Login a registered user"""
    # if request.method == "POST":
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return render("/")
    #     else:
    #         messages.success(
    #             request, "There was an error logging in, Please try again "
    #         )
    #         return redirect("login")
    # else:
    #     return render(request, "registration/login.html", {})

    if request.method():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user():
            login(request, user)
            return render("/")
        else:
            messages.success(request, ("There was a problem logging in."))
            return redirect("/login")
    else:
        return render(request, "registration/login.html", {})


def logout_view(request):
    """Log user out"""
    logout(request)
    return HttpResponseRedirect(redirect_to="/")


def register_user(request):
    """Make a new normal user"""
    if request.method != "POST":
        # Using the UserCreationForm
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                request, username=new_user.username, password=request.POST["password1"]
            )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("index"))
    context = {"form": form}
    return render(request, "registration/register.html", context)
