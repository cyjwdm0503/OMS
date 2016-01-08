from django.test import TestCase

# Create your tests here.
from django.test import  Client

client = Client()

client.get('/1/')