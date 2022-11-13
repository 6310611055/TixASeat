from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Customer, Product, Orders, Feedback
from django.urls import reverse
from django.contrib.auth import authenticate

class LoginTest(TestCase):
	
	def setUp(self):
		self.user = {
			'username': 'Taylor',
			'password': 'Taylor1234'
		}
		User.objects.create_user(**self.user)
		
	def test_correct_info(self):
		user = authenticate(username='Taylor', password='Taylor1234')
		self.assertTrue((user is not None) and user.is_authenticated)
  
	def test_wrong_username_input(self):
		user = authenticate(username='Selena', password='Taylor1234')
		self.assertFalse(user is not None and user.is_authenticated)
  
	def test_wrong_password_input(self):
		user = authenticate(username='Taylor', password='Taylor123')
		self.assertFalse(user is not None and user.is_authenticated)
	
class LoginFormTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="Taylor", password="Taylor123")

	def test_wrong_credentials(self):
		response = self.client.post(reverse('customerlogin'), 
			{ 'username' : 'taylor', 'password' : 'foofoo123'})
		self.assertEqual(response.status_code, 200)
	
	def test_correct_credentials(self):
		response = self.client.post(reverse('customerlogin'), 
			{ 'username' : 'Taylor', 'password' : 'Taylor123'}) 
		self.assertEqual(response.status_code, 302)
  
	def test_logout(self):
		response = self.client.post(reverse('logout'))
		self.assertTrue(response.status_code, 302)

#check product display on homepage
class homePageTestCase(TestCase):
	def setUp(self):
		superuser = User.objects.create_superuser(username='admin', password='102030')
  
		self.user = User.objects.create(username='Taylor', password='Taylor123')
		
		self.product1 = Product.objects.create(user=self.user, name='Taylor Swift', price=150, description='live in Bangkok',
											   seat='S13 R13', location='Rajamangala Stadium, Bangkok', time='08.00pm',
											   date='Dec 13, 2022', category='Concert', status='Available')

		self.product2 = Product.objects.create(user=self.user, name='Taylor Swift', price=150, description='live in Bangkok',
											   seat='S12 R13', location='Rajamangala Stadium, Bangkok', time='08.00pm',
											   date='Dec 13, 2022', category='Concert', status='Sold')
			 
	def test_product_available(self):
		self.assertEqual(self.product1.status, 'Available')
		
	def test_product_unavailable(self):
		self.assertEqual(self.product2.status, 'Sold')
		
	def test_product_price(self):
		self.assertEqual(self.product1.price, 150)

#check cart objects  
class cartViewTest(TestCase):
	
	def setUp(self):
		self.user = User.objects.create(username='Taylor', password='Taylor123')
  
		self.product1 = Product.objects.create(user=self.user, name='Taylor Swift', price=150, description='live in Bangkok',
											   seat='S13 R13', location='Rajamangala Stadium, Bangkok', time='08.00pm',
											   date='Dec 13, 2022', category='Concert', status='Available')
  
	def delete_product_from_cart(self):
		self.product1.delete()
		self.assertEqual(self.product1.count(), 0)

#test customer signup page			
class signupPageTest(TestCase):
	def setUp(self):
		self.firstname = 'Taylor'
		self.lastname = 'Swift'
		self.username = 'Taylor'
		self.password = 'Taylor123'
		
	def test_signup_form(self):
		response = self.client.post(reverse('customersignup'), data ={
			'username' : self.username,
			'password' : self.password,
			'firstname': self.firstname,
			'lastname' : self.lastname,
		})
		
		self.assertEqual(response.status_code, 302)
  
#admin part of the website
class adminViewsTestCase(TestCase):
    
    def setUp(self):
        self.name = "BLACKPINK"
        self.price = 250
        self.description = "Live in United Center!"
        self.seat = "S10 R02"
        self.location = "Chicago"
        self.date = "Nov 10, 2022"
        self.time = "08.00pm"
        
    def test_admin_add_product_form(self):
        response = self.client.post(reverse('admin-products'), data={
			'name' 		 : self.name,
			'price'		 : self.price,
			'description': self.description,
			'seat'  	 : self.seat,
			'location'	 : self.location,
			'date'		 : self.date,
			'time'		 : self.time,
		})
        
        self.assertEqual(response.status_code, 302)
        

        
	
		
