from django.shortcuts import render,redirect
from django.views import View
from .models import customer,Product
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
# Create your views here.
def base(request):
    return render(request,'mainapp/home.html')

def store(request):
    product={
        'product':Product.objects.all()
    }
    return render(request,'mainapp/store.html',product)


#locals() is a built in function to call all the local functions
class Category(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,'mainapp/category.html',locals())

class ProductDetails(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'mainapp/productdetais.html', locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,'mainapp/category.html',locals())



def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.order_by('-crated_date').filter(description__icontains=keyword)
            # product_count = product.count()
        else:
            return redirect('home')
    contxt = {
        'product' : product,
        # 'product_count' : product_count,
    }
    return render(request,'mainapp/store.html',contxt)


class CustomerRegistration(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'mainapp/Registration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulation User Registration Succesfull")
        else:
            messages.warning(request,'Invalid Input Data')
        return render(request, 'mainapp/Registration.html', locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'mainapp/profile.html', locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request, "congratulation profile created Succesfully")
        else:
            messages.warning(request, 'Invalid Input Data')
        return render(request, 'mainapp/profile.html', locals())

def Address(request):
    # add is store all data in user and it will iterated in address.html
    add = customer.objects.filter(user=request.user)
    return render(request,'mainapp/address.html',locals())

class AddresUpdate(View):
    def get(self,request,pk):
        add = customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'mainapp/updateAddress.html', locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.state = form.cleaned_data['state']
            add.save()
            messages.success(request, "congratulation profile Update Succesfully")
        else:
            messages.warning(request, 'Invalid Input Data')
        return redirect('address')


def loggout(request):
    logout(request)
    return redirect('login')


