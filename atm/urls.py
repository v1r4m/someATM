from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage, name='manepage'),
    path('balance/<int:cardnum>/<int:input>/', views.Balance_list, name='Balance_list'),
    path('insert/<int:cardnum>/', views.selectCard, name='selectCard'),
    path('pin/<int:cardnum>/<int:input>/', views.MatchCardAndPin, name='MatchCardAndPin'),
    path('deposit/<int:cardnum>/<int:money>', views.Deposit, name='Deposit'),
]
#is it safe to pass the insecured information through parameter in URL?
#if we use django in only backend system...