from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    # address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    CATEGORY =(
        ('Concert', 'Concert'),
        ('Musical', 'Musical'),
        ('Sport', 'Sport'),
        ('Other', 'Other')
    )
    STATUS=(
        ('Available', 'Available'),
        ('Sold', 'Sold')
    )
    # user=models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    seat=models.CharField(max_length=20, null=True)
    location=models.CharField(max_length=64, null=True)
    date=models.CharField(max_length=40, null=True)
    time=models.CharField(max_length=12, null=True)
    category=models.CharField(max_length=50,null=True,choices=CATEGORY)
    status=models.CharField(max_length=50,null=True,choices=STATUS, default='Available')
    def __str__(self):
        return f'{self.name} Seat: {self.seat} Date: {self.date} Category: {self.category} Status: {self.status}'


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Successful','Successful'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
