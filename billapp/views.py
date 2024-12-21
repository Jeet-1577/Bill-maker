from django.shortcuts import render
from billapp.models import Contact, Product
from django.contrib import messages
from math import ceil


# Create your views here.
def index(request):

# logic to create intem boxes by user>

    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods }
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}

    return render(request,"index.html", params)

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

