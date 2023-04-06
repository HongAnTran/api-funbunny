
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)
urlpatterns = [
    path('',views.index , name='index'),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/',views.UsertList.as_view() , name='users_list'),
    path('user/<int:pk>/', views.UserDetail.as_view(),name='users_detail'),
    path('transaction/',views.TransactionList.as_view() , name='transaction_list'),
    path('transaction/<int:pk>',views.TransactionDetail.as_view() , name='transaction_detail'),

]