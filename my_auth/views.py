from django.views import View
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode 
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email Is Taken")
                return render(request, 'signup.html')

                # return HttpResponse("Email already exit")
                # messages.warning(request,"Email is Taken")
        
        except Exception as identifier:
            pass
# Change this line: 


        user = User.objects.create_user(email,email, password)
        # user.set_password(password)        
        user.is_active=False
        user.save()
        
        message=render_to_string('activate.html',{
            'user':user,
#-----------------------------When hosting website change dominname-------------------------------------------------------------
            'domain' : '127.0.0.1:8000',
            'uid' :urlsafe_base64_encode(force_bytes(user.pk)), #storing userid in encoding formate
            'token':generate_token.make_token(user)
        
        })
       
    # sendin email with content

        # message = ''' hii this is massage of email'''
        email_subject =' this is mail of accouunt activation'
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,"Activate Your Account by clicking  the link in your gmail")
        return redirect('/auth/login/')
    return render(request, "signup.html")
    # return HttpResponse("User created", email)

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifire:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        return render(request,'activatefail.html')





def handlelogin(request):

    return render(request, "login.html")

def handlelogout(request):
    return redirect('/auth/login')
