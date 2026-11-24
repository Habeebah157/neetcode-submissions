from collections import OrderedDict
 
class LRUCache:
 
    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    # nós return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't encontrar the chave in out dict / cache.
    # And also move the chave to the end
    # to show that it was recently used.
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    # first, nós add / update the chave by conventional methods.
    # And also move the chave to the end to show that it was recently used.
    # But here nós will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so nós remove the primeiro chave (least recently used)
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
 