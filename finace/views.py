from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import  Transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import  TransactionSerializer , UserSerializer
from django.core.paginator import Paginator
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User


@api_view(['GET'])
def index(request):
    routes = [
        'token/',
        'token/refresh/',
        'transaction/',
        'user/'
    ]

    return Response(routes)



class UsertList(APIView):
    """
    List all user, or create a new new user.
    """
    def get(self, request, format=None):
        limit = request.query_params.get('limit')
        page_default = 1
        page_number = request.query_params.get('page_number' , page_default) 
        queryset = User.objects.all()
        
        if limit:
            paginator = Paginator(queryset, limit)
            page = paginator.page(page_number)
            users = page.object_list
        else:
            users = queryset

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if User.objects.filter(username = data['username']).first():
            return Response( "This username is already taken", status=status.HTTP_400_BAD_REQUEST)
       
       
        user = User.objects.create_user(data['username'],data['email'], data['password'])
        user.save()
        return Response("register success", status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class TransactionList(APIView):
    """
    List all transaction, or create a new new transaction.
    params : 
        + date_from? : Date  = thời gian bắt đầu  
        + date_to? : Date  = thời gian cuối mặc định là thời gian hiện tại
        + oder_by? :str = flied cần sắp xếp giảm dần thêm dấu - mặc định sắp xếp theo date
        + limit? : number = truyền vào nếu cần phân trang hoặc limit 
        + page_number? : number =  trang cần lấy mặc đinh là 1
    """
    # def get(self, request : Request, ):
        # Transaction.objects.delete()
        # records = Transaction.objects.all()
        # records.delete()
    def get(self, request : Request, format=None):
        # uid = request.query_params.get('uid')
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to' , datetime.now())
        order_by = request.query_params.get('order_by' , 'date')
        limit = request.query_params.get('limit')
        page_default = 1
        page_number = request.query_params.get('page_number' , page_default) 
        if date_from:
            queryset = Transaction.objects.filter(date__gt=date_from).filter(date__lte=date_to)
        else:
            queryset = Transaction.objects.all().order_by(order_by)

        if limit:
            paginator = Paginator(queryset, limit)
            page = paginator.page(page_number)
            users = page.object_list
        else:
            users = queryset

        serializer = TransactionSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetail(APIView):
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, pk):
        Transaction = self.get_object(pk)
        serializer = TransactionSerializer(Transaction)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        Transaction = self.get_object(pk)
        serializer = TransactionSerializer(Transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Transaction = self.get_object(pk)
        Transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 