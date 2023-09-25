from . import views
from django.urls import path
app_name='bankapp'
urlpatterns = [
    path('',views.bank_details,name='bank_details'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('details/',views.details,name='details'),
    path('logout',views.logout,name='logout'),
    path('home1/',views.home1,name='home1'),
    path('cust_all_details/',views.cust_all_details,name='cust_all_details'),
    path('ajax_handler/<int:id>/',views.ajax_handler,name='ajax_handler'),

]