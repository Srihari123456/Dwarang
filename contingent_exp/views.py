from django.shortcuts import render,get_object_or_404,redirect
from .models import Contingent_exp
from .forms import ContingentForm
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
def contingent_create_view(request):
    form = ContingentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContingentForm()

    context = {
        'form' : form
    }
    return render(request,"contingent_exp/contingent_create.html",context)

@login_required(login_url="/login/create_acc/")
def contingent_delete_view(request,tit,emp):
    try:
        queryset = Contingent_exp.objects.all().filter(employee_id=emp)
        #obj = get_object_or_404(Reimbursement,name=tit)
    except:
        redirect("../../../../dashboard/actions/contingent_gateway")
    else:
        if request.method == "POST":
           lista = []
           for j in queryset:
               lista.append(j)


           lengths = 0
           while 1:
               try:
                   print(bool(lista[lengths]))
                   lengths = lengths + 1
               except:
                   break

           if lengths == 1:
               queryset.delete()
           else:
               i = 0
               p = 0
               while i < lengths:
                   try:
                       print(bool(lista[i + 1]))
                       print(lista)
                       lista.remove(lista[i])
                       queryset[p].delete()
                       lengths = lengths - 1
                       p = p + 1
                   except:
                       break

           return redirect('../../../../dashboard/actions/contingent_gateway')
        context = {
            "object":queryset
        }
        return render(request,"contingent_exp/contingent_delete.html",context)


@login_required(login_url="/login/create_acc/")
def contingent_update_view(request,tit,emp):
    try:
        obj = get_object_or_404(Contingent_exp,name=tit)
    except:
        print("hi")
        return redirect("../../../../dashboard/actions/contingent_gateway")
    else:
        if obj.employee_id != emp:
            return redirect("../../../../dashboard/actions/contingent_gateway")
        else:
            form = ContingentForm(request.POST or None, instance=obj)
            if form.is_valid():
                form.save()
            context = {
                'form': form
            }
            return render(request, "contingent_exp/contingent_create.html", context)


#class GeneratePDF(View):
@login_required(login_url="/login/create_acc/")
def GeneratePDF(request,tit,emp, *args, **kwargs):
    template = get_template('contingent_exp/contingent_exp_form.html')
    try:
        obj = get_object_or_404(Contingent_exp, name=tit)
    except:
        print("hi")
        return redirect("../../../../dashboard/actions/contingent_gateway")
    else:
        print(BASE_DIR, "hey shrihari")

        context = {
            "object": obj,
            "today": datetime.date.today(),
            "n": obj.name,
            "base_dir": BASE_DIR,
        }
        if obj.employee_id != emp:
            return redirect("../../../../dashboard/actions/contingent_gateway")
        html = template.render(context)
        pdf = render_to_pdf('contingent_exp/contingent_exp_form.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "ContingentExpenditure_%s.pdf" % (context["n"])
            content = "inline; filename=%s" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment;filename=%s" % (filename)
            response['Content-Disposition'] = content
            # return HttpResponse(html)
            return response
            # return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not found")
        # return HttpResponse(html)

