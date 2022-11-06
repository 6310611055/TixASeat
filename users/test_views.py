from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Customer, Product, Orders, Feedback
from django.urls import reverse


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
  
  
class SignupFormTest(TestCase):
	
	def test_short_password(self):
		response = self.client.post(reverse('customersignup'), 
			{'username' : 'Taylor', 'password' : 'foo'})
		self.assertEqual(response.status_code, 302)
		
	def test_empty_passwords(self):
		response = self.client.post(reverse('customersignup'),
			{'username' : 'Taylor', 'password' : ''})
		self.assertEqual(response.status_code, 302)
	
	def test_set_name(self):
		doc = self.save({
			'fullname': 'Peter Miller',
		})
		assert doc.select(".alert-success")
		self.user = User.objects.get(pk=self.user.pk)
		assert self.user.fullname == 'Peter Miller'
  
class Test_list(TestCase):
	
	def test_project_list_POST(self):
		client = Client()
		
		response = client.post(reverse('list'))
		
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'book/customersignup.html')
	
		
