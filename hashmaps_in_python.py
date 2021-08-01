# Python implementation of a hashmap.
# so hashmaps are already implemented in python in the python dictionary.
# but for the sake of understanding hashmaps more deeply I am re-implementing hashmaps in python in this file



def __init__(self):
    pass

def _get_hash(self, key):
    pass


def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    if self.map[key_hash] is None:
        self.map[key_hash] = list([key_value])
        return True
    else:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.map[key_hash].append(key_value)
        return True

def get(self, key):
    pass

def delete(self, key):
    pass