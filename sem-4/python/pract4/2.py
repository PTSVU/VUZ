class HashTable:
    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for i, (k, _) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        for k, v in self.data:
            if k == key:
                return v
        raise KeyError(f'Key not found: {key}')

    def __contains__(self, key):
        return any(k == key for k, _ in self.data)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.data):
            result = self.data[self._index]
            self._index += 1
            return result
        raise StopIteration

    def get(self, key, default=None):
        for k, v in self.data:
            if k == key:
                return v
        return default


ht = HashTable()

ht['key1'] = 'value1'
ht['key2'] = 'value2'

assert ht['key1'] == 'value1'
assert ht['key2'] == 'value2'

assert 'key1' in ht
assert 'key3' not in ht

assert len(ht) == 2

for key, value in ht:
    print(f'{key}: {value}')

assert ht.get('key1') == 'value1'
assert ht.get('key3', 'default') == 'default'

for pair in ht:
    print(pair)

