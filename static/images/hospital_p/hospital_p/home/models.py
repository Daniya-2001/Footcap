from django.db import models
import os
import datetime
def get_file_path(request,filename):
    orginal_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%n%d%H:%%M:%S')
    filename="%s%s"% (nowTime,orginal_filename)
    return os.path.join('uploads/',filename)
# Create your models here.
class Department(models.Model):
    slug=models.CharField(max_length=100,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Docter(models.Model):
    docter=models.ForeignKey(Department,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    docter_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.CharField(max_length=500,null=False,blank=False)
   
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    created_at=models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name
class Booking(models.Model):
    p_name=models.CharField(max_length=250)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Docter,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.p_name
        