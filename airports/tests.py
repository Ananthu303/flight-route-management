"""
Tests for the Airport Routes System.
"""

from django.test import TestCase, Client
from django.urls import reverse
from .models import AirportRoute


class AirportRouteModelTests(TestCase):
    """Test cases for the AirportRoute model."""
    
    def setUp(self):
        """Set up test data."""
        # Create a simple tree structure
        # Root -> Left -> LeftLeft
        #      -> Right
        
        self.left_left = AirportRoute.objects.create(
            airport_code='LLL',
            position='Level-2-Left',
            duration=30
        )
        
        self.left = AirportRoute.objects.create(
            airport_code='LEFT',
            position='Level-1-Left',
            duration=45,
            left=self.left_left
        )
        
        self.right = AirportRoute.objects.create(
            airport_code='RIGHT',
            position='Level-1-Right',
            duration=60
        )
        
        self.root = AirportRoute.objects.create(
            airport_code='ROOT',
            position='Root',
            duration=90,
            left=self.left,
            right=self.right
        )
    
    def test_airport_creation(self):
        """Test that airports are created correctly."""
        self.assertEqual(AirportRoute.objects.count(), 4)
        self.assertEqual(self.root.airport_code, 'ROOT')
        self.assertEqual(self.root.duration, 90)
    
    def test_get_last_reachable_left(self):
        """Test finding the last reachable node going left."""
        last_node = self.root.get_last_reachable_node('left')
        self.assertEqual(last_node.airport_code, 'LLL')
    
    def test_get_last_reachable_right(self):
        """Test finding the last reachable node going right."""
        last_node = self.root.get_last_reachable_node('right')
        self.assertEqual(last_node.airport_code, 'RIGHT')
    
    def test_get_longest_duration(self):
        """Test finding the airport with longest duration."""
        longest = AirportRoute.get_airport_with_longest_duration()
        self.assertEqual(longest.airport_code, 'ROOT')
        self.assertEqual(longest.duration, 90)
    
    def test_get_shortest_duration(self):
        """Test finding the airport with shortest duration."""
        shortest = AirportRoute.get_airport_with_shortest_duration()
        self.assertEqual(shortest.airport_code, 'LLL')
        self.assertEqual(shortest.duration, 30)


class AirportRouteViewTests(TestCase):
    """Test cases for the views."""
    
    def setUp(self):
        """Set up test client and data."""
        self.client = Client()
        self.airport = AirportRoute.objects.create(
            airport_code='TEST',
            position='Test Position',
            duration=50
        )
    
    def test_home_view(self):
        """Test the home page loads correctly."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'airports/home.html')
    
    def test_airport_list_view(self):
        """Test the airport list view."""
        response = self.client.get(reverse('airport_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TEST')
    
    def test_add_airport_view_get(self):
        """Test the add airport form loads."""
        response = self.client.get(reverse('add_airport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'airports/add_airport.html')
    
    def test_longest_duration_view(self):
        """Test the longest duration view."""
        response = self.client.get(reverse('longest_duration'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TEST')
    
    def test_shortest_duration_view(self):
        """Test the shortest duration view."""
        response = self.client.get(reverse('shortest_duration'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TEST')
