import random
from django.shortcuts import render
from.models import  Category,Product,Cart,Profile,Order,OrderItem
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import  User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    
    
    return render(request,"index.html")

def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")  
            return redirect('register')  
        else:
         user=User.objects.create_user(username=username,email=email,password=password)
         user.save();
        return redirect('/')
    else:
     return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/') 
def products(request,slug):
     if(Category.objects.filter(slug=slug,status=0)):
        product=Product.objects.filter(category__slug=slug)
     else:
        messages.warning(request,"no collections found")
        return redirect('collections')
     return render(request,"products.html",{"product":product})


def productsview(request,cate_slug,prod_slug):
     if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            aswin=Product.objects.filter(slug=prod_slug,status=0)
        else:
          messages.error(request,"no such product found")
          return redirect('collections')

     else:
        messages.error(request,"no such category found")
        return redirect('collections')
     return render(request,"productsview.html",{"aswin":aswin})
 

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                     return JsonResponse({'status':"product already in cart"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quntity >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"product added successfully"})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quntity)+" quantity avilable"})                 
            else:
                return JsonResponse({'status':"no such product found"})
        else:
                 return JsonResponse({'status':"Login to continue"})
        
    return redirect('/')

def cart(request):
    cart=Cart.objects.filter(user=request.user)
    
    return render(request,"cart.html",{"cart":cart})

def delete_data(request,id):
   
        pi=Cart.objects.get(pk=id)
        pi.delete()
        messages.info(request,"deleted ")
        return redirect('cart') 
    

def checkout(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quntity :
            Cart.objects.delete(id=item.id)
            ###################################
            
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems :
        total_price = total_price + item.product.selling_price * item.product_qty
     
     
    userprofile = Profile.objects.filter(user=request.user).first()
        
    context={'cartitems':cartitems,'total_price':total_price,'userprofile':userprofile}        
    return render(request,"checkout.html",context)

def placeorder(request):
    
    if request.method == "POST":
        
        ####
        currentuser =User.objects.filter(id=request.user.id).first()
        
        if not currentuser.username :
            currentuser.first_name = request.POST.get('name')
            currentuser.save()
            
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.name = request.POST.get('name')
            userprofile.email = request.POST.get('email')
            userprofile.phone = request.POST.get('phone')
            userprofile.country = request.POST.get('country')
            ##userprofile.state = request.POST.get('state')
            userprofile.city = request.POST.get('city')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.Address = request.POST.get('Address')
            userprofile.save()
             
     
            
           
            
        ####
        neworder = Order()
        neworder.user = request.user
        neworder.name = request.POST.get('name')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.country = request.POST.get('country')
        ##neworder.state = request.POST.get('state')
        neworder.city = request.POST.get('city')
        neworder.pincode = request.POST.get('pincode')
        neworder.Address = request.POST.get('Address')
        
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')
        
        cart = Cart.objects.filter(user=request.user)
        cart_totall_price = 0
        for item in cart :
            cart_totall_price = cart_totall_price + item.product.selling_price * item.product_qty
            
        neworder.total_price = cart_totall_price
        
        trackno = 'aswin'+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno)is None :
            trackno = 'aswin'+str(random.randint(1111111,9999999))
              
        neworder.tracking_no = trackno
        neworder.save()
    
        
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems :
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )     
            
            ###decress 
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quntity = orderproduct.quntity - item.product_qty
            orderproduct.save()
            
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"Your order has been placed successfully")  
            
        payMode = request.POST.get('payment_mode')
        if(payMode == "Paid by Razorpay"):
            return JsonResponse({"status":"Your order has been placed successfully"})
    return redirect('cart')


def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart :
        total_price = total_price + item.product.selling_price * item.product_qty
    return  JsonResponse({
        'total_price' : total_price
    })
    
 
def orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request,"oreders.html",context)   

 





def orderview(request,t_no):
    order =Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order,'orderitems':orderitems}
    return render(request,"orderview.html",context)  


def orders(request):
    orders= Order.objects.filter(user=request.user)
    context = {"orders":orders}  
    return render(request,"orders.html",context)

def orderview(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order,'orderitems':orderitems}
    return render(request,"orderview.html",context)
        

    
 


# Create your views here.
@login_required(login_url='login')
def shop(request):
    category=Category.objects.filter(status=0)
    
    return render(request,"shop.html",{"category":category})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")