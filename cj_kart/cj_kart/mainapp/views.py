from django.shortcuts import render
from django.views import View
from .models import Product,customer
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
# Create your views here.
def base(request):
    return render(request,'mainapp/home.html')

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