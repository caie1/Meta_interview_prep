class Node:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.prev,self.next=None,None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}#hashmap to store key-node pair where node pointing to value of its key
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    # node is always middle of other nodes
    #if its first node, then its middle of left and right node
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next,nxt.prev=nxt,prev
    #insert alwasy happens on previous node of right node as its most recent used node
    def insert(self,node):   
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.prev,node.next=prev,nxt
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            #remove left key which is LRU
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

#Unit testing module for above code
import unittest

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.cache = LRUCache(2)  # Create an LRUCache with capacity 2

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

    def test_cache_eviction_order(self):
        """Test that cache evicts in the correct order."""
        self.cache.put(1, 1)
        self.cache.put(2, 2)
        self.cache.get(1)  # Access key 1
        self.cache.put(3, 3)  # Should evict key 2 (least recently used)
        self.assertEqual(self.cache.get(2), -1)  # Should return -1 (not found)
        self.assertEqual(self.cache.get(1), 1)  # Should return 1
        self.assertEqual(self.cache.get(3), 3)  # Should return 3

    def test_capacity_one(self):
        """Test behavior with a cache capacity of one."""
        self.cache = LRUCache(1)  # Create an LRUCache with capacity 1
        self.cache.put(1, 1)
        self.assertEqual(self.cache.get(1), 1)  # Should return 1
        self.cache.put(2, 2)  # Evicts key 1
        self.assertEqual(self.cache.get(1), -1)  # Should return -1 (not found)
        self.assertEqual(self.cache.get(2), 2)  # Should return 2

    def test_invalid_key(self):
        """Test get with an invalid key."""
        self.assertEqual(self.cache.get(999), -1)  # Should return -1 (not found)

if __name__ == '__main__':
    unittest.main()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
