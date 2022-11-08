from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage, name='manepage'),
    path('balance/<int:cardnum>/<input>/', views.Balance_list, name='Balance_list'),
    path('balance_all/<int:userid>/<input>/',views.Balance_all_list, name='Balance_all_list'),
    path('insert/<int:cardnum>/', views.selectCard, name='selectCard'),
    path('pin/<int:cardnum>/<input>/', views.MatchCardAndPin, name='MatchCardAndPin'),
    path('deposit/<int:cardnum>/<input>/<int:money>', views.Deposit, name='Deposit'),
    path('Withdraw/<int:cardnum>/<input>/<int:money>', views.Withdraw, name='Withdraw'),
    path('newregister/<int:userid>/<int:cardnum>/<input>', views.newregister, name='newregister'),
]
#is it safe to pass the insecured information through parameter in URL?
#if we use django in only backend system...