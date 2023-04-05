from django.db import models
import datetime
# Create your models here.


typeTransaction_CHOICES = (
        ( 'spending' ,'tiêu dùng'),
        (  'income' ,'thu nhập' ),
)
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=100) 
    displayName=models.CharField(max_length=20)
    photoURL = models.URLField(blank=True , null=True)
    phoneNumber = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return str(self.id) +  ' ' +  self.displayName

class Transaction(models.Model):

    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    typeTransaction = models.CharField(max_length=30 , choices=typeTransaction_CHOICES , default='spending')
    idCategory = models.CharField(max_length=30)
    note = models.TextField(blank=True , null=True)
    imageDescription = models.URLField(blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) +  ' ' + self.uid.displayName + ' ' + str(self.value) 
    

