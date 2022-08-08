import json
from decimal import Decimal
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_swagger.views import get_swagger_view
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import AccountSerializer
from .models import Account

# Create your views here.

schema_view = get_swagger_view(title='Bank API')

account_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'balance': openapi.Schema(type=openapi.TYPE_NUMBER, description='decimal')
    },
    required=['name', 'balance']
)

transaction_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={        
        'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='decimal')
    },
    required=['amount']
)

##
# This view handles the creation of a bank account.
# Takes a name and balance and creates a new account on the database
##
@swagger_auto_schema(method='post', request_body=account_request, responses={200: "OK", 400: "Bad Request"})
@api_view(('POST',))
def Create_Account(request):   
    serializer = AccountSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response("ok")


##
# This view Retrieves an account by name and
# returns an object with the account name and balance
# or returns a 404 if no account is found
##
@swagger_auto_schema(method='get', responses={200: "OK", 404: "Not Found"})
@api_view(('GET',))
def Get_Account(_, name):    
    account = get_account_or_404(name)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

##
# This view handles account deposits:
# retrieves an account by name and adds the given amount to the account balance
##
@swagger_auto_schema(method='post', request_body=transaction_request, responses={200: "OK", 404: "Not Found"})
@api_view(('POST',))
def Deposit(request, name):
    account = get_account_or_404(name)    
    amount = request.data['amount']
    account.balance += Decimal(amount)
    account.save()
    return Response("ok")

##
# This view handles account deposits:
# retrieves an account by name and subtracts the given amount from the account balance
##
@swagger_auto_schema(method='post', request_body=transaction_request, responses={200: "OK", 404: "Not Found"})
@api_view(('POST',))
def Withdraw(request, name):
    account = get_account_or_404(name)    
    amount = request.data['amount']
    account.balance -= Decimal(amount)
    account.save()
    return Response("ok")


def get_account_or_404(name):
    queryset = Account.objects.all()
    account = get_object_or_404(queryset, name=name)
    return account
