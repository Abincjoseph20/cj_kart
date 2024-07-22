from django.shortcuts import render
from django.views import View
# Create your views here.
def base(request):
    return render(request,'mainapp/home.html')

class CatagoryView(View):
    def get(self,request):
        return render(request,'mainapp/catagory.html')