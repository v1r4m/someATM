from django.contrib import admin
from .models import Card
from .models import User
# Register your models here.
admin.site.register(Card)
admin.site.register(User)