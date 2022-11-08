from django.shortcuts import render
from .models import Card, User
import hashlib

def mainpage(request):
    return render(request, 'atm/main.html')

def selectCard(request,cardnum):
    selectedCard = Card.objects.filter(cardNumber = cardnum)
    selectedCard[0].isInserted = True
    return selectedCard[0]


def MatchCardAndPin(request,cardnum, input):
    userIdt = (Card.objects.filter(cardNumber=cardnum))[0].cardUser
    print(userIdt)
    password = (User.objects.filter(userId=userIdt))[0].PinNumber
    inputhash = hashlib.sha256(input.encode())
    if password==inputhash:
        return True
    else:
        return False

def Balance_list(request, cardnum, input):
    Balances = Card.objects.filter(cardNumber=cardnum)
    if MatchCardAndPin(request,cardnum,input):
        return render(request, 'atm/deposit_list.html', {'Balances':Balances})
    else:
        return "Pin is wrong"

def Deposit(request,cardnum, money):
    card = Card.objects.filter(cardNumber = cardnum)
    card[0].Balance = card[0].Balance+money

def Withdraw(request,cardnum, money):
    card = Card.objects.filter(cardNumber=cardnum)
    leftmoney = card[0].Deposit
    if leftmoney > money:
        card[0].Balance = card[0]


# Create your views here.
