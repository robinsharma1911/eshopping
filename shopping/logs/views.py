from django.shortcuts import render,redirect

from .models import log_db
from .forms import LoginForm,RegisterForm
# Create your views here.

#==============Login======================
def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)              #store login form information in 'form' variable and check validation............
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if log_db.objects.filter(email=email,password=password):
                request.session['email'] = email
                return redirect('/carts')
            else:
                login_form = LoginForm()               #store login from in a variable to pass in login.html as context......
                return render(request,'logs/login.html',{'loginform':login_form})

    else:
        login_form = LoginForm()               #store login from in a variable to pass in login.html as context......
        return render(request,'logs/login.html',{'loginform':login_form})

#==============Registration======================
def registration(request):

    if request.method == 'POST':                         
        form = RegisterForm(request.POST)                   #store register form information in a variable 'form' and check validation.............
        if form.is_valid():                                 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            if log_db.objects.filter(email=email):   #check if email  is exists() in database........
                pass
                
            elif log_db.objects.filter(phone=phone):  #check if phone no. is already exists in database....
                pass
            else:
                #_________save registraion of a user into database___________
                db = log_db(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
                db.save()
                #________set email as sessionn after register a new user and go to carts________
                request.session['email'] = email
                return redirect('/carts')
    else:            
        register_form = RegisterForm()
        return render(request,'logs/registration.html',{'registerform':register_form})

#===============Logout========================
def logout(request):
    del request.session['email']
    return redirect('/')