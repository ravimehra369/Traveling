from django.shortcuts import render,HttpResponse
from myapp.models import contact


# Create your views here.

def index(request):
    # return HttpResponse("<h3>this is heading</h3>")
    context = {"variable" : "variabl data"}

    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'about.html')


def services(request):
    # return HttpResponse("<h1>this is serveces page</h1>")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("<h1>this is contacts page</h1>")    
    
    if request.method =="POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        contact1 = contact(name = name, lastname = lname, email = email )
        
    return render(request, 'contact.html')




# def index(request):
#     data1 = "inside views data1"
    
#     data2 = "inside views data2"
      
#     context = {'variable1':data1,'variable2':data2}
  
#     return render(request, 'index.html', context)    
