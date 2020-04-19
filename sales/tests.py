from django.test import TestCase
from sales.models import Order
from django.contrib.auth.models import User
from restaurant.models import Restaurant

class OrderTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
        username='javed', email='javed@javed.com', password='my_secret')
        restaurant = Restaurant.objects.create(name='Restaurant 1', content='Some description about restaurant',owner=user)
        Order.objects.create(user_id=user, order_total=1235, seller_id=restaurant)

    def test_restaurant_name(self):
        order = Order.objects.get(order_total =1235)
        self.assertEqual(order.seller_id.name, "Restaurant 1")



