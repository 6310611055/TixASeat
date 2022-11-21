from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Customer, Product, Orders, Feedback,Payment
from django.urls import reverse
from django.contrib.auth import authenticate
from http.cookies import SimpleCookie
		
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
  
	def test_home_view_url_without_login(self):
		# url = reverse("tixaseat:homePage")
		# self.client.cookies.load({'product_ids': '1|1'})
		url = reverse("homePage")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
  
	def test_home_view_url_with_login(self):
		self.client.login(username="", password="")
		url = reverse("homePage")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
  


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

class TestCookieFunction(TestCase):
		
	def test_home_view_cookie(self):
		self.client.cookies = SimpleCookie({'test_cookie': 'test_value'})
		response = self.client.get('users/index.html')

		self.assertEqual(response.client.cookies['test_cookie'].value, 'test_value')
  
	def test_cart_view_cookie(self):
		self.client.cookies = SimpleCookie({'test_cookie': 'test_value'})
		response = self.client.get('users/cart.html')

		self.assertEqual(response.client.cookies['test_cookie'].value, 'test_value')
  
	def test_search_view_cookie(self):
		self.client.cookies = SimpleCookie({'test_cookie': 'test_value'})
		response = self.client.get('users/navbar.html')

		self.assertEqual(response.client.cookies['test_cookie'].value, 'test_value')
  
	def test_add_to_cart_view_cookie(self):
		self.client.cookies = SimpleCookie({'test_cookie': 'test_value'})
		response = self.client.get('users/customer_add_products.html')

		self.assertEqual(response.client.cookies['test_cookie'].value, 'test_value')
  
	def test_remove_from_cart_view_cookie(self):
		self.client.cookies = SimpleCookie({'test_cookie': 'test_value'})
		response = self.client.get('users/customer_remove_product.html')

		self.assertEqual(response.client.cookies['test_cookie'].value, 'test_value')

#Test image performance
class image_file_models_test(TestCase):

	def create_image_file(self, content="simple content"):
		upload_file = open('/django_blog_it/static/favicon.png', 'rb')
		return Image_File.objects.create(Image_File=upload_file, thumbnail=upload_file, upload=upload_file)

	def test_category_creation(self):
		w = self.create_image_file()
		self.assertTrue(isinstance(w, Image_File))
		self.assertEqual(w.__str__(), str(w.date_created())) 
		
class ProductFormTest(TestCase):
	def test_forms(self):
		form_data = {'product_id': '1'}
		form = ProductForm(data=form_data)
		self.assertTrue(form.is_valid())
		
class CustomerFormTest(TestCase):
	def test_forms(self):
		form_data = {'firstname': 'Taylor',
					 'lastname' : 'Swift',
					 }
		form = CustomerForm(data=form_data)
		self.assertTrue(form.is_valid())
		
#Test cart functionality

class TestCartPosition(TestCase):
	TEST_CARTPOSITION_RES = {
		'id': 1,
		'cart_id': 'aaa@api',
		'item': 1,
		'variation': None,
		'price': '23.00',
		'attendee_name_parts': {'full_name': 'Taylor'},
		'attendee_name': 'Taylor',
		'attendee_email': None,
		'datetime': '2018-06-11T10:00:00Z',
		'expires': '2018-06-11T10:00:00Z',
		'includes_tax': True,
		'seat': None,
		'answers': []
	}

	def test_cartposition_detail(token_client, organizer, event, item, taxrule, question):
		testtime = datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC)

		with mock.patch('django.utils.timezone.now') as mock_now:
			mock_now.return_value = testtime
			cr = CartPosition.objects.create(
				event=event, cart_id="aaa@api", item=item,
				price=23, attendee_name_parts={'full_name': 'Peter'},
				datetime=datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC),
				expires=datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC)
			)
		res = dict(TEST_CARTPOSITION_RES)
		res["id"] = cr.pk
		res["item"] = item.pk
		resp = token_client.get('/api/v1/organizers/{}/events/{}/cartpositions/{}/'.format(organizer.slug, event.slug,
																					   cr.pk))
		assert resp.status_code == 200
		assert res == resp.data
  
	def test_cartposition_delete(token_client, organizer, event, item, taxrule, question):
		testtime = datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC)
		with mock.patch('django.utils.timezone.now') as mock_now:
			mock_now.return_value = testtime
			cr = CartPosition.objects.create(
				event=event, cart_id="aaa@api", item=item,
				price=23, attendee_name_parts={'full_name': 'Peter'},
				datetime=datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC),
				expires=datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC)
			)
			CartPosition.objects.create(
				event=event, cart_id="aaa@api", item=item, addon_to=cr,
				price=23, attendee_name_parts={'full_name': 'Peter'},
				datetime=datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC),
				expires=datetime.datetime(2018, 6, 11, 10, 0, 0, 0, tzinfo=UTC)
			)
		res = dict(TEST_CARTPOSITION_RES)
		res["id"] = cr.pk
		res["item"] = item.pk
		resp = token_client.delete('/api/v1/organizers/{}/events/{}/cartpositions/{}/'.format(organizer.slug, event.slug,
																						  cr.pk))
		assert resp.status_code == 204
		
	def test_cartposition_create_with_seat(token_client, organizer, event, item, quota, seat, question):
		res = copy.deepcopy(CARTPOS_CREATE_PAYLOAD)
		res['item'] = item.pk
		res['seat'] = seat.seat_guid
		resp = token_client.post(
			'/api/v1/organizers/{}/events/{}/cartpositions/'.format(
				organizer.slug, event.slug
			), format='json', data=res
		)
		assert resp.status_code == 201
		with scopes_disabled():
			p = CartPosition.objects.get(pk=resp.data['id'])
		assert p.seat == seat
  
class TestPayment(TestCase):
	
	def test_download_invoice(self):
		url = reverse("download-invoice", args=[1,1])
		response = self.client.get(url)
		self.assertEqual(response.status_code, 302)
  
	def test_delete_invoice(self):
		user = User.objects.create_user(username='Taylor', password='Taylor123')
		login = self.client.login(username='Taylor', password="Taylor123") 
		# self.payment = Payment.objects.create(user=user, date="13 Dec, 2022", time="11.00 AM",
		#                                 amount=120, last4=1234)
		url = reverse("delete-payment", args=[1])
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_admin_payment_check(self):
		user = User.objects.create_user(username='admin', password='admin')
		login = self.client.login(username='admin', password='admin') 
		# print(login)
		# self.payment = Payment.objects.create(user=user, date="13 Dec, 2022", time="11.00 AM",
		#                                 amount=120, last4=1234)
		url = reverse("admin-payment")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
  
class AboutusPage(TestCase):
	def aboutus_view_test(self):
		url = reverse("aboutus")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed("users/aboutus.html")
  
class ProductPage(TestCase):
	def test_customer_delete_product(self):
		user = User.objects.create_user(username='Taylor', password='Taylor123')
		login = self.client.login(username='Taylor', password='Taylor123') 
		url = reverse("my-products")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 302)   
  
class ProfilePage(TestCase):
	def test_my_profile_view(self):
		user = User.objects.create_user(username='Taylor', password='Taylor123')
		login = self.client.login(username='Taylor', password='Taylor123') 
		url = reverse("my-profile")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 302)
			 
		

		

	
		
	
		
