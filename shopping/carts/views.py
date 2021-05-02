from django.shortcuts import render,redirect

# Create your views here.

def carts(request):
    if request.session.has_key('email'):
        email = request.session['email']
        return render(request,'carts/cart.html',{'email':email})
    else:
        return redirect('/logs/')
    
    