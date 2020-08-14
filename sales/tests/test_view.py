from django.test import TestCase


class MyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_something(self):
        self.assertEqual(True, True)


