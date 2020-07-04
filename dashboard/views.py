from django.shortcuts import render,get_object_or_404,redirect
from .forms import ActionForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/create_acc/")
def dashboard_view(request):
    return render(request,"dashboard.html",context={})

@login_required(login_url="/login/create_acc/")
def actions_form_view(request,pg):
    if request.method == 'POST':
        form = ActionForm(data=request.POST)
        name = request.POST.get('name')
        employee_id = request.POST.get('employee_id')
        print("User Name = ", name)
        print("Password = ", employee_id)
        redir_page = pg+'.html'
        print(redir_page)
        if form.is_valid():
            form.save()
            return render(request, redir_page, {'form': form,'name':name,'employee_id':employee_id})
    else:
        form = ActionForm()
    return render(request, "pre-entry.html", {'form':form})

