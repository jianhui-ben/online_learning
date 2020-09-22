
class LRU_Cache:

    def __init__(self, capacity=5):
        # Initialize class variables
        self.dic={}   ##quickly retrieve data
        self.used= []  ##find the oldest item
        self.length=0   ## curent length
        self.capacity=capacity  ##capacity limit

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dic:
            ## change the appearing order of this key
            self.used.remove(key)
            self.used.append(key)
            return self.dic[key]
        return -1

    def set(self, key, value):
        if self.capacity<=0:
            print('zero capacity')
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.length< self.capacity:
            self.length+=1
        else:
            old_key= self.used.pop(0)
            _ = self.dic.pop(old_key, None)

        self.dic[key]=value
        self.used.append(key)
            
# test case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# test case 2:  empty cache Null capacity or 0 capacity
cache_2=LRU_Cache(0)
cache_2.get(1)

cache_2.set(1,2)
cache_2.set(1,3)
cache_2.get(1)

# test case 3: 
cache_3=LRU_Cache(2)
cache_3.set(1, 1)

cache_3.set(2,2)
cache_3.set(1,3)
cache_3.get(1)

# test case 4: large cache
cache_4=LRU_Cache(100000)
for i in range(100000):
    cache_4.set(i, i)

cache_4.get(1)
cache_4.set(2,2)
cache_4.set(1,3)