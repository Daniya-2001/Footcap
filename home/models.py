from django.db import models
from django.contrib.auth.models import  User

import os
import datetime
def get_file_path(request,filename):
    orginal_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%n%d%H:%%M:%S')
    filename="%s%s"% (nowTime,orginal_filename)
    return os.path.join('uploads/',filename)
# Create your models here.
class Category(models.Model):
    
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default,1=Trending")
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name 
    
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
   
    name=models.CharField(max_length=100,null=False,blank=False)
    slug=models.CharField(max_length=100,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.CharField(max_length=500,null=False,blank=False)
    quntity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    created_at=models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name  
    
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at = models.DateField(auto_now_add=True)  



   
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    name = models.CharField(max_length=150,null=False)   
    email = models.CharField(max_length=150,null=False) 
    phone = models.CharField(max_length=150,null=False)
    country = models.CharField(max_length=150,null=False)
    
    city = models.CharField(max_length=150,null=False)
    pincode =models.CharField(max_length=150,null=False)
    Address =models.CharField(max_length=150,null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150,null=False)
    payment_id = models.CharField(max_length=250,null=True)
    orderstatuses =(
        ('Pending','Pending'),
        ('Out For shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150,choices=orderstatuses,default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return '{} .{}'.format(self.id, self.tracking_no)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    price =  models.FloatField(null=False)   
    quantity = models.IntegerField(null=False)
    
    def __str__(self):
        return '{} .{}'.format(self.order.id, self.order.tracking_no)
    
      
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)      
    phone=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=510,null=True)
    country=models.CharField(max_length=150,null=True)
    state=models.CharField(max_length=150,null=True)
    pincode=models.CharField(max_length=150,null=True)
    Address=models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.user.username
    

    # class Amodel(models.Model):
    #     name=models.CharField(max_length=100)
    #     email=models.EmailField(max_length=150)
    #     password=models.CharField(max_length=100)
    