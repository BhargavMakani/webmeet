from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def main_view(request):
    uname = request.user.username
    fullname=request.user.get_full_name().title()
    name = request.user.get_short_name().title()
    # context = {}
      # print(request.user.is_authenticated())
    print(uname)
    return render(request,'chat/main.html',{'uname':uname,'fullname':fullname,'name':name})
# def loginfunc(request):
#     if request.method == 'POST':
        
        
#     return render(request, 'chat/home.html')
 
def home(request): 
    return render(request, 'chat/home.html')

# def account(request):      
#     return render(request, 'chat/signup.html') 

def signupfunc(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pwd']
        cpassword = request.POST['cpwd']
        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname 
        myuser.save()
        messages.success(request,'your account has created')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('/join')
        
    # return render(request, 'chat/signup.html') 
        
    
def loginfunc(request):
    if request.method == 'POST':
        loginUname = request.POST['uname']
        loginPwd = request.POST['password']
        user = authenticate(username=loginUname,password=loginPwd)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('/join')
        else:
            messages.error(request,'invalid login')
            return HttpResponse('invalid login')
def leave(request):
    return render(request, 'chat/leave.html')
    
    
