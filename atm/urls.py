from django.urls import path
from . import views
urlpatterns = [
    path('balance/<int:userid>/', views.Balance_list, name='Balance_list'),
    path('insert/<int:cardNumber>/', views.selectCard, name='selectCard'),
    path('pin/<int:carNumber>/<int:pinNumber>/', views.MatchCardAndPin, name='MatchCardAndPin'),
    path('deposit/<int:cardNumber>/<int:money>', views.Deposit, name='Deposit'),
]
#is it safe to pass the insecured information through parameter in URL?
#if we use django in only backend system...