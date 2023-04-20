from django.http import HttpResponse
from django.shortcuts import render
from . models import placetab
def fan(request):
    insrt=placetab()
    insrt.name="for only emergency"
    insrt.desc="nbfbdjbhbfbd hfjjsj gjknjkng jfjg njjtha t ush hrhh hrhuhr huhuhf  huhuhhguhgh "
    return render(request,"index.html",{'insrtrslt':insrt})



def datas(request):
    username=request.POST["usrnme"]
    password=request.POST["pswrd"]
    return render(request,"datas.html",{'usr':username,'ps':password })


