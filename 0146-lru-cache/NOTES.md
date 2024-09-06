```
import unittest
​
class TestLRUCache(unittest.TestCase):
def setUp(self):
"""Set up the test environment before each test."""
self.cache = LRUCache(2)  # Create an LRUCache with capacity 2
​
def test_put_and_get(self):
"""Test basic put and get functionality."""
self.cache.put(1, 1)
self.cache.put(2, 2)
self.assertEqual(self.cache.get(1), 1)  # Should return 1
self.cache.put(3, 3)  # Evicts key 2
self.assertEqual(self.cache.get(2), -1)  # Should return -1 (not found)
self.cache.put(4, 4)  # Evicts key 1
self.assertEqual(self.cache.get(1), -1)  # Should return -1 (not found)
self.assertEqual(self.cache.get(3), 3)  # Should return 3
self.assertEqual(self.cache.get(4), 4)  # Should return 4
​
def test_update_existing_key(self):
"""Test that updating an existing key changes the value and order."""
self.cache.put(1, 1)
self.cache.put(2, 2)
self.cache.put(1, 10)  # Update key 1 to 10
self.assertEqual(self.cache.get(1), 10)  # Should return updated value 10
self.cache.put(3, 3)  # Evicts key 2, not key 1
self.assertEqual(self.cache.get(2), -1)  # Should return -1 (not found)
self.assertEqual(self.cache.get(1), 10)  # Should still return 10
self.assertEqual(self.cache.get(3), 3)  # Should return 3
​
def test_cache_eviction_order(self):
"""Test that cache evicts in the correct order."""
self.cache.put(1, 1)