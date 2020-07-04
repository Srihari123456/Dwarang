from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


def home_view(request,*args,**kwargs):
    print("Welcome ",request.user)
    return render(request,"home.html",{})
    
def about_view(request,*args,**kwargs):
    my_context = {}
    return render(request,"about.html",my_context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'base.html',{'form':form})
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


def logout_view(request,*args,**kwargs):
    logout(request)
    return render(request,"logout.html",{})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print("User Name = ", username)
        print("Password = ", password)

        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, '../../dashboard/templates/dashboard.html', {'form': form,'username':username})
    else:
        form = AuthenticationForm()
    return render(request,'signin.html',{'form':form})

