from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("tixaseat:homePage"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("tixaseat:"))
        self.assertTemplateUsed(response, "users/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("tixaseat:"))
        self.assertContains(response, "<h1>Upcoming Event</h1>")
        self.assertNotContains(response, "Not on the page")

class AboutPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/aboutus")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("aboutus"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("aboutus"))
        self.assertTemplateUsed(response, "users/aboutus.html")

class ConcertPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/concert")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("concert"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("concert"))
        self.assertTemplateUsed(response, "users/index_concert.html")

class MusicalPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/musical")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("musical"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("musical"))
        self.assertTemplateUsed(response, "users/index_musical.html")

class SportPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/sport")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("sport"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("sport"))
        self.assertTemplateUsed(response, "users/index_sport.html")

class OtherPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/other")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("other"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("other"))
        self.assertTemplateUsed(response, "users/index_other.html")

class CartPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/cart")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("cart"))
        self.assertTemplateUsed(response, "users/cart.html")

class CustomerLoginPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/customerlogin")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("customerlogin"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("customerlogin"))
        self.assertTemplateUsed(response, "users/customerlogin.html")

class AdminLoginPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/adminlogin")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("adminlogin"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("adminlogin"))
        self.assertTemplateUsed(response, "users/adminlogin.html")

class CustomerLogoutPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("logout"))
        self.assertTemplateUsed(response, "users/logout.html")
        