from django.shortcuts import render,get_object_or_404,redirect
from .models import TA_Bill
from .forms import TAForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from dashboard.utils import render_to_pdf
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@login_required(login_url="/login/create_acc/")
def ta_create_view(request):
    form = TAForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TAForm()

    context = {
        'form' : form
    }
    return render(request,"ta_bill/ta_create.html",context)


@login_required(login_url="/login/create_acc/")
def ta_delete_view(request,tit,emp):
    try:
        queryset = TA_Bill.objects.all().filter(employee_id=emp)
        #obj = get_object_or_404(Reimbursement,name=tit)
    except:
        redirect("../../../../dashboard/actions/tabill_gateway")
    else:

        if request.method == "POST":
           lista = []
           for j in queryset:
               lista.append(j)
               print(j.name)

           lengths = 0
           while 1:
               try:
                   print(bool(lista[lengths]))
                   lengths = lengths+1
               except:
                   break

           if lengths == 1:
               queryset.delete()
           else:
               i=0
               while i < lengths:
                   try:
                       print(bool(lista[i+1]))
                       print(lista)
                       lista.remove(lista[i])
                       queryset[0].delete()
                       lengths = lengths -1
                       #i = i+1
                   except:
                       break

           return redirect('../../../../dashboard/actions/tabill_gateway')
        context = {
            "object":queryset
        }
        return render(request,"ta_bill/ta_delete.html",context)




@login_required(login_url="/login/create_acc/")
def ta_update_view(request,tit,emp):
    try:
        obj = get_object_or_404(TA_Bill,name=tit)
    except:
        return redirect("../../../../dashboard/actions/tabill_gateway")
    else:
        if obj.employee_id != emp:
            return redirect("../../../../dashboard/actions/tabill_gateway")
        else:
            form = TAForm(request.POST or None,instance=obj)
            if form.is_valid():
                form.save()
            context = {
                'form':form
            }
            return render(request,"ta_bill/ta_create.html",context)


@login_required(login_url="/login/create_acc/")
def GeneratePDF(request,tit,emp, *args, **kwargs):
    template = get_template('ta_bill/ta_bill_form.html')
    try:
        obj = get_object_or_404(TA_Bill, name=tit)
    except:
        print("hi")
        return redirect("../../../../dashboard/actions/tabill_gateway")#HttpResponseNotFound("Sorry " + tit + " form not found")
    else:
        print(BASE_DIR,"hey shrihari")

        context = {
            "object":obj,
            "today": datetime.date.today(),
            "n":obj.name,
            "base_dir":BASE_DIR,
        }
        if obj.employee_id != emp:
            return redirect("../../../../dashboard/actions/tabill_gateway")
        html = template.render(context)
        pdf = render_to_pdf('ta_bill/ta_bill_form.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "TravellingAllowanceBill_%s.pdf" %(context["n"])
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment;filename=%s" %(filename)
            response['Content-Disposition'] = content
            #return HttpResponse(html)
            return response
            #return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not found")
        #return HttpResponse(html)
