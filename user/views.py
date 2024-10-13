from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        emails= CustomUser.objects.filter(email = email).exists()
        if not emails:
            msg = "Email Not found."
            messages.error(request, msg)
            return redirect(request.path)
        else:
            try:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    msg = "Login Successfully."
                    messages.success(request, msg)
                    return redirect('/adminpanel')
                else:
                    msg = "User Not found."
                    messages.error(request, msg)
            except Exception as e:
                print(e)
                messages.error(request, f'Failed'+str(e))

    return redirect('login_view')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('r_email')
        password = request.POST.get('r_password')
        c_password = request.POST.get('rc_password')

        if password != c_password:
            messages.error(request, 'Password Not matched')
            return redirect (request.path)
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Registerd Not matched')
            return redirect (request.path)
        else:
            try:
                user = CustomUser(
                    first_name = name,
                    email = email,
                )
                user.set_password(password)
                user.save()
                messages.success(request, 'User Register Successfully')
                return redirect (request.path)
            except Exception as e:
                print(e)
                messages.error(request, f'Failed'+str(e))
                return redirect (request.path)
    
    return redirect('login_view')

def logout_user(request):
    logout(request)
    if not logout:
         messages.error(request, 'Fail to Sign Out')
         return redirect(request.path)
    else:
        messages.success(request, 'Sign Out Successfully')
        return redirect('login_view')
    
def login_view(request):
    return render(request, 'user/login.html')