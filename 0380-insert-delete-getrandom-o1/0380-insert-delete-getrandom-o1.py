import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.val_index_map:
            return False
        self.val_index_map[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_index_map:
            return False
        index = self.val_index_map[val]
        last_val = self.vals[-1]
        self.vals[index] = last_val
        self.val_index_map[last_val] = index
        self.vals.pop()
        del self.val_index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
