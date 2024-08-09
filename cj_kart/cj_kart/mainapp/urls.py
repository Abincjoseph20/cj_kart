from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetpasswordform
urlpatterns = [

    path('',views.base,name='home'),
    path('store/', views.store, name='store'),
    path('categories/<slug:val>',views.Category.as_view(),name="category"),
    path('ProductDetais/<int:pk>/',views.ProductDetails.as_view(),name='Product_detais'),

    path('categories-title/<val>',views.CategoryTitle.as_view(),name="category-title"),

    path('search',views.search,name='search'),
    #registrations
    path('registrations',views.CustomerRegistration.as_view(),name="customer-registration"),

    #LoginView is a built-in function in django for using Login porpus
    path('accounts/login/',auth_view.LoginView.as_view(template_name='mainapp/login.html',authentication_form=LoginForm),name='login'),

    #user profile urls if login success then go to this function
    path('profile/',views.ProfileView.as_view(),name='profiles'),

    #for display address
    path('addres',views.Address,name='address'),

    #for edit address
    path('UpdateAddress/<int:pk>',views.AddresUpdate.as_view(),name='AddresUpdates'),

    #auth_view.PasswordChangeView.as_view is buit in function to use change password
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='mainapp/ChangePassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),

    #auth_view.PasswordChangeDoneView.as_view
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='mainapp/PasswordChangedone.html'),name="PasswordChangedone"),

    #auth_view.LogoutView.as_view built  in functionfor logout
    #path('logout',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('logout/', views.loggout, name='logout'),





    # PasswordResetView is built-in function using password reset or Forgot Password for login time
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='mainapp/password_reset.html',form_class=MyPasswordResetForm), name='pswd_reset'),

    # PasswordResetDoneView is built-in function using password reset or Forgot Password done for login time
    path('password_reset_done', auth_view.PasswordResetDoneView.as_view(template_name='mainapp/password_reset_done.html'), name='password_reset_done'),

    # PasswordResetConfirmView is built-in function using password reset or Forgot Password done for login time
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='mainapp/password_reset_confirm.html',form_class=MySetpasswordform), name='password_reset_confirm'),

    # PasswordResetCompleteView is built-in function using password reset or Forgot Password done for login time
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='mainapp/password_reset_complete.html'),name='password_reset_complete'),

    #path('password_reset/',auth_view.PasswordResetView.as_view(),name='password_reset')

]
