from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreate,ProfileUpdate,ProfileImageUpdate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = UserCreate()
    context = {
        'form':form
    }
    return render(request,'signup.html',context)

@login_required
def profile(request):
    if request.method == "POST":
        u_form = ProfileUpdate(request.POST,instance=request.user)
        i_form = ProfileImageUpdate(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and i_form.is_valid():
            u_form.save()
            i_form.save()
            messages.info(request,'your account has been updated')
            return redirect('profile')
    else:
        u_form = ProfileUpdate(instance= request.user)
        i_form = ProfileImageUpdate(instance= request.user.profile)

        context = {
            "u_form":u_form,
            "i_form":i_form
        }
        return render(request,'profile.html',context)