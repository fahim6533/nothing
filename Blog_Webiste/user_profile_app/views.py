from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.
from .forms import User_registration_form,user_login_form,user_profile_update
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .decorators import not_logged_in_required
from .models import User


@never_cache
@not_logged_in_required
def login_user(request):
    form=user_login_form()

    if request.method=="POST":
        form = user_login_form(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,"Worng Information")

    context={
        "form":form
    }

    return render(request,"login.html",context)




def logout_user(request):
    logout(request)
    return redirect('login')






@never_cache
@not_logged_in_required
def register_user(request):
    form = User_registration_form()

    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registration sucessful")
            return redirect('login')

    context = {
        "form": form
    }
    return render(request, 'signup.html', context)



@login_required(login_url='login')
def profile(request):
    account= get_object_or_404(User,pk=request.user.pk)
    form=user_profile_update(instance=account)
    if request.method == "POST":
        if request.user.pk != account.pk:
            return redirect('home')
        form=user_profile_update(request.POST,instance=account)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile has been updated sucessfully")
            return redirect('profile')
        print("Posted")
    else:
        print("problem")
        
    context={
        "account":account,
        "form":form
    }
    return render(request,'profile.html',context)


@login_required
def change_profile_picture(request):
    if request.method == "POST":
        
        form=user_profile_update(request.POST,request.FILES)
        
        if form.is_valid():
            image=request.FILES['profile_images']
            user=get_object_or_404(User,pk=request.user.pk)
            
            if request.user.pk != user.pk:
                return redirect('home')
            
            user.profile_image = image
            user.save()
            messages.success(request,"Profile image updated successfully")
            return redirect ('profile')


