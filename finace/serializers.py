from rest_framework import serializers 


from .models import  Transaction
from django.contrib.auth.models import User

class TransactionSerializer(serializers.ModelSerializer):
   class Meta:
        model = Transaction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = '__all__'