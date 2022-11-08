from django.shortcuts import render
from .models import Card, User
import hashlib

def selectCard(cardN):
    selectedCard = Card.objects.filter(cardNumber = cardN)
    selectedCard[0].isInserted = True
    return selectedCard[0]


def MatchCardAndPin(cardnum, input):
    password = (User.objects.filter(cardUser=cardnum))[0].PinNumber
    inputhash = hashlib.sha256(input.encode())
    if password==inputhash:
        return True
    else:
        return False

def Balance_list(request, cardnum):
    Balances = Card.objects.filter(cardNumber=cardnum)
    return render(request, 'atm/deposit_list.html', {'Balances':Balances})

def Deposit(cardnum, money):
    card = Card.objects.filter(cardNumber = cardnum)
    card[0].Balance = card[0].Balance+money

def Withdraw(cardnum, money):
    card = Card.objects.filter(cardNumber=cardnum)
    leftmoney = card[0].Deposit
    if leftmoney > money:
        card[0].Balance = card[0]


# Create your views here.
