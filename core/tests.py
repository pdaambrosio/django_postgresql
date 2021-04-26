from django.test import TestCase

def add_num(num):
    return num + 1

class SimpleTestCase(TestCase):

    def setUp(self):
        self.numero = 41

    def test_add_num(self):
        val = add_num(self.numero)
        self.assertTrue(val == 42)