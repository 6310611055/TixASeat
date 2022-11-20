from django.test import TestCase
from users.models import Customer, Product, Orders, Feedback, Payment
from django.contrib.auth.models import User

class TestCustomerModel(TestCase):
	def setUp(self):
		self.T1 = User.objects.create_user(username="Taylor_Swift",
									 password="Taylor1313", 
									 first_name="Taylor", 
									 last_name="Swift")
		self.user = Customer.objects.create(user=self.T1, mobile="+4457678667" )
	  
	def test_customer_str(self):
		self.assertEqual(self.user.__str__(), self.T1.first_name)
  
	def test_customer_get_id(self):
		usr_id = self.T1.id
		self.assertEqual(self.user.get_id(), usr_id)
  
	def test_customer_get_name(self):
		get_name = self.T1.first_name+" "+self.T1.last_name
		self.assertEqual(self.user.get_name(), get_name)
  

class TestProductModel(TestCase):
	def setUp(self):
		self.usr = User.objects.create_user(username="Taylor_Swift",
									 password="Taylor1313", 
									 first_name="Taylor", 
									 last_name="Swift")
		self.product = Product.objects.create(user=self.usr, name="BLACKPINK",
                                        seat="S01R02",
                                        price=250,
                                        date="10 Nov, 2022",
                                        category="concert",
                                        status="Available",
                                        )
	def test_product_str(self):
		self.assertEqual(self.product.__str__(), f'{self.product.name} Seat: {self.product.seat} Date: {self.product.date} Category: {self.product.category} Status: {self.product.status}')