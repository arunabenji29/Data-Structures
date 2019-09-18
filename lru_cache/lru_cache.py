import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=3):
    self.max = limit
    self.dll = DoublyLinkedList()
    self.dict = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.dict:
      current = self.dll.head

      while current:
        if current.value == key:
          print(f'get: If i have the same key')
          self.dll.move_to_end(current)
          return self.dict[key]
        current = self.dll.head.next
    else:
      return None


  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if self.dll.__len__() == self.max:
      if key in self.dict:
        current = self.dll.head

        while current:
          if current.value == key:
            print(f'set:for max length: If i have the same key')
            self.dict[key] = value
            self.dll.move_to_end(current)
            break
          current = self.dll.head.next

      else:
        print('set:for max length: if no key exists')
        self.dict[key] = value
        self.dll.remove_from_head()
        self.dll.add_to_tail(key)
      

    elif self.dll.__len__() < self.max:
      if key in self.dict:
        current = self.dll.head

        while current:
          if current.value == key:
            print(f'set: If i have the same key')
            self.dict[key] = value
            self.dll.move_to_end(current)
            break
          current = self.dll.head.next

      else:
        print('set: if no key exists')
        self.dict[key] = value
        self.dll.add_to_tail(key)
        # print(f'set: head is {self.dll.head.value}')
    print(f'set: dict is {self.dict}')
      

lru = LRUCache()
print(lru.get('item1'))

lru.set('item1',1)
lru.set('item2',2)
lru.set('item3',3)
print(lru.get('item1'))
print(lru.get('item2'))
print(lru.get('item3'))    
lru.set('item4',4)
# print(lru.get('item1'))
# print(lru.get('item3'))  
print(lru.get('item4'))
print(lru.get('item1'))