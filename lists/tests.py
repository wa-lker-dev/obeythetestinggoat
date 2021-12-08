from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    def test_fail():
        assert 42 == 1