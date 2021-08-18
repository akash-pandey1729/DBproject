from core.forms import DataForm
from core.forms import ApplicationForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

val = 0
def get_quote(dict):
    if(dict['Income_Group']=="Low Income"):
        if(dict['Insurance_Product']== "P1"):
            return "500 USD"
        if(dict['Insurance_Product']== "P2"):
            return "1000 USD"
        if(dict['Insurance_Product']== "P3"):
            return "1500 USD"
        if(dict['Insurance_Product']== "P4"):
            return "2000 USD"
        else:
            return "Error in the details entered. Please try again"

    if(dict['Income_Group']=="Middle Income"):
        if(dict['Insurance_Product']== "P1"):
            return "1000 USD"
        if(dict['Insurance_Product']== "P2"):
            return "1500 USD"
        if(dict['Insurance_Product']== "P3"):
            return "2000 USD"
        if(dict['Insurance_Product']== "P4"):
            return "2500 USD"
        else:
            return "Error in the details entered. Please try again"

    if(dict['Income_Group']=="High Income"):
        if(dict['Insurance_Product']== "P1"):
            return "2000 USD"
        if(dict['Insurance_Product']== "P2"):
            return "2500 USD"
        if(dict['Insurance_Product']== "P3"):
            return "3000 USD"
        if(dict['Insurance_Product']== "P4"):
            return "3500 USD"
        else:
            return "Error in the details entered. Please try again"

    print(dict['Income_Group'], dict['Insurance_Product'])
    return "Error in the details entered. Please try again"

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            x = form.save()
            print(form.cleaned_data)
            val = get_quote(form.cleaned_data)
            print(val)
            #print("x is",x.id)
            #return redirect('showquote.html')
            return render(request, 'showquote.html', {'form_data': form,'getquote':val,'id':x.id})
    form = DataForm()
    return render(request, 'index.html', {'form': form})

def appview(request,pk):
    print(pk)
    print("Here")
    if request.method == 'POST':
        appform = ApplicationForm(request.POST)
        print("inside if")
        print(appform.errors)
        if appform.is_valid():
            x = appform.save()
            print(appform.cleaned_data)
            print("Look")
            return render(request, 'result.html')
    instance = Data.objects.get(pk=pk)
    appform = ApplicationForm(initial = {"fkey_Do_Not_Change":pk,"Lifestyle_Variables":instance.Lifestyle_Variables,"First_Name":instance.First_name,"Last_Name":instance.Last_Name,"Income_Group": instance.Income_Group, "Morbidity_History":instance.Morbidity_History,"Sex":instance.gender,"Insurance_Product":instance.Insurance_Product})
    return render(request, 'application.html', {'appform': appform})