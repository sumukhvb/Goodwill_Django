from django.test import TestCase

# Create your tests here.
from ..homepage.models import Section

print(Section.objects.all())