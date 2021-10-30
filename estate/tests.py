from django.test import TestCase
from .models import Neighborhood,Business

# Create your tests here.
      
   
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighbourhood = Neighborhood('karen','Nairobi',56)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, Neighborhood))

    def test_update_neighborhood(self):
        self.new_neighborhood.save_hood()
        neighborhood_id = self.new_neighbourhood.id
        Neighborhood.update_hood(id, "mombasa")
        self.assertEqual(self.neighborhood.neighborhood,"mombasa")

    def test_delete_neighborhood(self):
        self.new_neighbourhood.save_hood()
        self.neighborhood.delete_hood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods) == 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_business = Business(biz_name ='Zaimet',biz_email = 'zaimet@food.com', biz_description='Eat good Live good', biz_digits='0791122323')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_update_business(self):
        self.new_business.save_business()
        business_id = self.new_business.id
        Business.update_business(id, "ZaimetKiller")
        self.assertEqual(self.business.business, "ZaimetKiller")

    def test_delete_business(self):
        self.business.save_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)