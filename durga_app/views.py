from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import ContactData

def ContactView(request):
    if request.method=='POST':
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1=request.POST.get('name','')
            salary1=request.POST.get('salary','')
            email1=request.POST.get('email','')
            city1=request.POST.get('city','')
            data=ContactData(
                name=name1,
                salary=salary1,
                email=email1,
                city=city1,
            )
            data.save()
            cform=ContactForm()
            return render(request,'contact.html',{'abc':cform})
        else:
            return HttpResponse("Invalid Form")
    else:
        cform=ContactForm()
        return render(request,'contact.html',{'abc':cform})