from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm
urlpatterns = [

    path('',views.base,name='home'),
    path('categories/<slug:val>',views.Category.as_view(),name="category"),
    path('ProductDetais/<int:pk>/',views.ProductDetails.as_view(),name='Product_detais'),
    path('categories-title/<val>',views.CategoryTitle.as_view(),name="category-title"),

    #registrations
    path('registrations',views.CustomerRegistration.as_view(),name="customer-registration"),

    #LoginView is a built-in function in django for using Login porous
    path('accounts/login/',auth_view.LoginView.as_view(template_name='mainapp/login.html',authentication_form=LoginForm),name='signin'),

    #PasswordResetView is built-in function using password reset
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='mainapp/password_reset.html',form_class=MyPasswordResetForm),name='pswd_reset'),

    #user profile urls if login success then go to this function
    path('profile/',views.ProfileView.as_view(),name='profiles'),

    #for display address
    path('addres',views.Address,name='address'),
]
