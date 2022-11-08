from django.db import models

class User(models.Model):
    userId = models.IntegerField()
    PinNumber = models.CharField(max_length=64) #SHA-256. you can have many card, but your pincode is only one in one bank.
                                                # i don't know if this really happens in real bank but I make my account in this way.

# Create your models here.
class Card(models.Model):
    cardNumber = models.CharField(max_length=16)
    Balance = models.PositiveBigIntegerField()
    Deposit = models.PositiveBigIntegerField()
    Withdraw = models.PositiveBigIntegerField()
    isInserted = models.BooleanField(default=False)
    cardUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def getCardNumber(self):
        return self.cardNumber

