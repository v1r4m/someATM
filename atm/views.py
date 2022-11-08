from django.shortcuts import render
from django.http import HttpResponse
from .models import Card, User
import hashlib

def mainpage(request):
    return render(request, 'atm/main.html')

def selectCard(request,cardnum):
    try:
        selectedCard = Card.objects.filter(cardNumber = cardnum)
        selectedCard[0].isInserted = True
        return HttpResponse("Hello, user Id - "+str(selectedCard[0].cardUser.userId)+", plz log in with localhost:8000/insert/(cardNumber)/(password)")
    except:
        return HttpResponse("no such id")

def MatchCardAndPin(request,cardnum, input):
    userIdt = (Card.objects.filter(cardNumber=cardnum))[0].cardUser.userId
    password = User.objects.filter(userId=userIdt)[0].PinNumber
    inputhash = hashlib.sha256(input.encode()).hexdigest()
    if password==inputhash:
        return True
    else:
        return False

def Balance_list(request, cardnum, input):
    try:
        Balances = Card.objects.filter(cardNumber=cardnum)
        if MatchCardAndPin(request,cardnum,input):
            return render(request, 'atm/deposit_list.html', {'Balances':Balances})
        else:
            return HttpResponse("pw incorrect")
    except:
        return HttpResponse("no such id")

def Balance_all_list(request, userid, input):
    try:
        searchUser = User.objects.filter(userId=userid)
        Balances = Card.objects.filter(cardUser=searchUser[0])
        if searchUser[0].PinNumber==hashlib.sha256(input.encode()).hexdigest():
            return render(request, 'atm/deposit_list.html', {'Balances':Balances})
        else:
            return HttpResponse("pw incorrect")
    except:
        return HttpResponse("no such id")

def Deposit(request,cardnum, input, money):
    card = Card.objects.filter(cardNumber = cardnum)
    if MatchCardAndPin(request,cardnum,input):
        tem = card[0].Balance+money
        card.update(Balance=tem)
        print(card[0].Balance)
        return HttpResponse("okay, money left "+str(card[0].Balance))
    else:
        return HttpResponse("pw incorrect")

def Withdraw(request,cardnum,input, money):
    card = Card.objects.filter(cardNumber=cardnum)
    if MatchCardAndPin(request,cardnum,input):
        leftmoney = card[0].Balance
        if leftmoney > money:
            tem = card[0].Balance-money
            card.update(Balance=tem)
            card[0].isInserted = False # card went out
            return HttpResponse("okay, money left "+str(card[0].Balance))
        else:
            return HttpResponse("you can't withdraw more money than you have.")
    else:
        return HttpResponse("pw incorrect")

def newregister(request, userid, cardnum, input):
    isR = User.objects.filter(userId=userid)
    isA = Card.objects.filter(cardNumber=cardnum)
    if (len(isR)==0 & len(isA)==0): #unregistered one
        newU = User(userId=userid, PinNumber=hashlib.sha256(input.encode()).hexdigest())
        newU.save()
        newA = Card(cardNumber=cardnum, Balance=1000, isInserted=False, cardUser=newU)
        newA.save()
        return HttpResponse("welcome, user "+str(userid))
    elif (len(isR)==0 & len(isA)==1): #duplicated cardnumber
        return HttpResponse("duplicated card number. choose another.")
    elif (len(isR)==1):
        if isR[0].PinNumber == hashlib.sha256(input.encode()).hexdigest() :
            if len(isA)==0:
                newA = Card(cardNumber=cardnum, Balance=1000, isInserted=False, cardUser=isR[0])
                return HttpResponse("we add another card for you, user "+str(userid))
            else:
                return HttpResponse("duplicated card number. choose another.")
        else:
            return HttpResponse("password incorrect. if you are trying to register, try to choose another user id.")


# Create your views here.
