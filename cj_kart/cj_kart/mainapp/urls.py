from django.urls import path
from . import views
urlpatterns = [

    path('',views.base,name='home'),
    path('catagory',views.CatagoryView.as_view(),name='catagory'),
]
