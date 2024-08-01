from django.shortcuts import render,redirect
from django.views import View
from .models import customer,Products
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.
def base(request):
    return render(request,'mainapp/home.html')

#locals() is a built in function to call all the local functions
class Category(View):
    def get(self,request,val):
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title')
        return render(request,'mainapp/category.html',locals())

class ProductDetails(View):
    def get(self, request,pk):
        product = Products.objects.get(pk=pk)
        return render(request, 'mainapp/productdetais.html', locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Products.objects.filter(title=val)
        title = Products.objects.filter(category=product[0].category).values('title')
        return render(request,'mainapp/category.html',locals())


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

# def addtocart(request):
#     user = request.user
#     product_id = request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Kart(user=user,product=product).save()
#     return redirect('/cart')

# def showcart(request):
#     user = request.user
#     cart = Kart.objects.filter(user=user)
#     return render(request,'mainapp/addtocart.html',locals())
