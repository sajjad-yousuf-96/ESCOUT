from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('product/<str:pk>',views.product,name='product'),
    path('database/',views.databasePage,name='database'),
    path('profitcalculator/',views.profitcalculator,name='profitcalculator'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutP,name='logout'),
    path('commission/',views.darazCommission,name='daraz_commission'),
    path('exporttocsv/',views.exporttocsv,name='exporttocsv'),
    # exporttocsv/
    path('productcalculator/',views.productcalculator,name='productcalculator'),
    path('keywordtracking/',views.keywordtracking,name='keywordtracking'),
    path('datacompetitor/',views.datacompetitor,name='datacompetitor')
]