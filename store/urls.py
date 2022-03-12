from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),	    
	path('logout/', views.logoutUser, name="logout"),
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('signup/', views.signup, name='signup'),
]