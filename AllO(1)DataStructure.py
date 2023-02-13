class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key2value = {}
        self.value2key = collections.defaultdict(set)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key2value:
            self.value2key[self.key2value[key]].remove(key)
            if not self.value2key[self.key2value[key]]:
                del self.value2key[self.key2value[key]]
            self.key2value[key] += 1
            self.value2key[self.key2value[key]].add(key)
        else:
            self.key2value[key] = 1
            self.value2key[1].add(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key2value:
            self.value2key[self.key2value[key]].remove(key)
            if not self.value2key[self.key2value[key]]:
                del self.value2key[self.key2value[key]]
            if self.key2value[key] == 1:
                del self.key2value[key]
            else:
                self.key2value[key] -= 1
                self.value2key[self.key2value[key]].add(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.value2key:
            return next(iter(self.value2key[max(self.value2key)]))
        else:
            return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.value2key:
            return next(iter(self.value2key[min(self.value2key)]))
        else:
            return ""
        
