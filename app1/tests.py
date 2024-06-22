from os import name
from django.test import TestCase
from app1.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound='roar')
    def test_animal_can_speak(self):
        lion =Animal.objects.get(name="lion")
        self.assertEqual(lion.speak(3), "roarroarroar")
        self.assertEqual(lion.count(3), 9)
        self.assertEqual(lion.meat(3), 'nead 9kg meat!')

