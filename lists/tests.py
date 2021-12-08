from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home

class TestHome(TestCase):
    def test_home(self):
        found = resolve('/')
        assert found.func == home

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home(request)  
        html = response.content.decode('utf8')  
        assert html.startswith('<html>') 
        assert '<title>To-Do lists</title>' in html
        assert html.endswith('</html>')