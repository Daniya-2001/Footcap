
from django.urls import path
from.import views



urlpatterns = [
    
    path('',views.home,name="home"),
    path('login',views.loginn,name="login"),
    path('logout',views.logout,name="logout"),
    path('register',views.register,name="register"),
    path('shop',views.shop,name="shop"),
    
    path('add-to-cat',views.addtocart,name="addtocart"),
    path('products/<str:cate_slug>/<str:prod_slug>',views.productsview,name="productview"),
    path('products/<str:slug>',views.products,name="product"),
    path('add-to-cat',views.addtocart,name="addtocart"),
    path('cart',views.cart,name="cart"),
    path('delete/<int:id>/', views.delete_data,name="delete"),
    path("checkout",views.checkout,name="checkout"),
    path('placeorder',views.placeorder,name="placeorder"),
    
    path('proceed-to-pay',views.razorpaycheck,name="razorpaycheck"),
    path('my-orders',views.orders,name="orders"),
    path('view-order/<str:t_no>',views.orderview,name="orderview"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    # path('add',views.add,name="add"),
   
    
]
