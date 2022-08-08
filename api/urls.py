from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('account/', views.Create_Account, name="account_create"),
    path('account/<str:name>/', views.Get_Account, name="account_detail"),    
    path('account/<str:name>/deposit', views.Deposit, name="account_deposit"),
    path('account/<str:name>/withdraw', views.Withdraw, name="account_withdraw"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]