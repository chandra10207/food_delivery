# from django.test import TestCase
# from django.urls import reverse, resolve
# # from .views import home, board_topics, new_topic
# from restaurant.models import Restaurant
#
# class RestaurantTests(TestCase):
#     def setUp(self):
#         Restaurant.objects.create(name='Django', content='Some Text',owner=1)
#
#     def test_board_topics_view_success_status_code(self):
#         url = reverse('boards:board_topics', kwargs={'pk': 5})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)


from django.test import TestCase
from restaurant.models import Restaurant

class RestaurantTestCase(TestCase):
    def setUp(self):
        Restaurant.objects.create(name='Mecca', content='Some Text',owner=1)

    def test_restaurant_name(self):
        """Animals that can speak are correctly identified"""
        restaurant_name = Restaurant.objects.get(name="Mecca")
        self.assertEqual(restaurant_name, 'Mecca')