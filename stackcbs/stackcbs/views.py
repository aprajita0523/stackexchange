from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def home_view(request):
    user = request.user
    hello ="hello world"
    #return HttpResponse('hello stack exchnage')
    #in template we send the key 
    context = {
        'user_t':user,
        'hello_t':hello
        }
    return render(request,'main/home.html',context)

def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('login')
    context = {'form':form} 
    return render(request,'main/register.html',context)    

def login_page(request):
    if request.method == 'POST':
        
        context = {}
    return render(request,'main/login.html',context)        