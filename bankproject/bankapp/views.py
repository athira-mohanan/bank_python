from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import Branch, Cust_details,Sub_branch


def bank_details(request):
    obj=Branch.objects.all()
    return render(request,"index.html",{'result':obj})

def login(request):
    obj = Branch.objects.all()
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['username'] = 'username'
            request.session['password'] = 'password'
            auth.login(request,user)
            return render(request,"home.html")
        else:
            messages.info(request,"Invalid credentials")
            return redirect('/login')
    return render(request,"login.html",{'result':obj})

def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    obj = Branch.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpwd=request.POST['cpwd']
        if password == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request,"passwords not match")
    return render(request,"register.html",{'result':obj})

def home(request):
    obj = Branch.objects.all()
    return render(request,"home.html",{'result':obj})

def details(request):
    branch=Branch.objects.all()
    if request.method =='POST':
        cust_name = request.POST.get('cust_name',)
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        branch = request.POST.get('branch', )# corresponding branch id
        branch_instance = Branch.objects.get(pk=branch)  # Retrieve a Branch instance by primary key
        city = request.POST.get('city', )
        city_instance = Sub_branch.objects.get(pk=city)
        account_type = request.POST.get('account_type', )
        material = request.POST.get('material', )
        customer= Cust_details(cust_name=cust_name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,branch_id=branch,sub_branch_id=city,material=material,account_type=account_type)
        customer.save();
        messages.info(request,"Application accepted")
        return redirect('/home1')

    # branch_list=Branch.objects.all()
    return render(request,"details.html",{'result':branch})

def home1(request):
    obj = Branch.objects.all()
    return render(request,"home1.html",{'result':obj})

def ajax_handler(request,id):
    cities = Sub_branch.objects.filter(branch__id=id).values_list('id','sub_name')
    # print(cities)
    cities = dict(cities)
    return JsonResponse({
        'cities' : cities,
    })

def cust_all_details(request):
    obj = Branch.objects.all()
    all_cust =Cust_details.objects.all()
    paginator = Paginator(all_cust, 6)
    try:
        current_page = int(request.GET.get('page', '1'))
    except:
        current_page = 1
    try:
        cust_per_page = paginator.page(current_page)
    except (EmptyPage, InvalidPage):
        cust_per_page = paginator.current_page(paginator.num_pages)

    return render(request,"customer_details.html",{'all_cust':cust_per_page,'result':obj})