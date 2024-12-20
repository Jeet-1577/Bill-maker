from django.shortcuts import render
from billapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        desc =request.POST.get("desc")
        email = request.POST.get("email")
        pnumber = request.POST.get("pnumber")
        myquery = Contact(name=name, email=email, desc=desc, pnumber=pnumber)
        myquery.save()
        messages.info(request, "we will get back to you soon....")

    return render(request,"contact.html")

def about (request):
    return render(request,"about.html")

