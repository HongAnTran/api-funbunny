from django.db import models
import datetime
# Create your models here.
from django.contrib.auth.models import User

typeTransaction_CHOICES = (
        ( 'spending' ,'tiêu dùng'),
        (  'income' ,'thu nhập' ),
)
class Transaction(models.Model):

    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    # uid = models.ForeignKey(User , on_delete=models.CASCADE)
    value = models.FloatField(default=0)
    typeTransaction = models.CharField(max_length=30 , choices=typeTransaction_CHOICES , default='spending')
    idCategory = models.CharField(max_length=30)
    note = models.TextField(blank=True , null=True)
    imageDescription = models.URLField(blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) +  ' ' + self.user_id.get_username() + ' ' + str(self.value) 
    

