from django.urls import path
from .views import home,checkout,pesan,keranjang,login
urlpatterns = [
    path('', home, name='home.html'),
    path('checkout', checkout, name='checkout.html'),
    path('pesan', pesan, name='pesan.html'),
    path('keranjang', keranjang, name='keranjang.html'),
    path('login', login, name='login.html')
]