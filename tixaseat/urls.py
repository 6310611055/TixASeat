"""tixaseat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='users/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('concert', views.catagory_concert,name='concert'),
    path('musical', views.catagory_musical,name='musical'),
    path('sport', views.catagory_sport,name='sport'),
    path('other', views.catagory_other,name='other'),
    path('my-order', views.my_order_view,name='my-order'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='users/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('cart', views.cart_view,name='cart'),

]

