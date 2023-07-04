class HashTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i, value in self.data_map[index]:
                if i == key:
                    return value
        return None

    def keys(self):
        all_keys = []
        for index in self.data_map:
            if index:
                for entry in index:
                    all_keys.append(entry[0])
        return all_keys



table = HashTable()
table.set_item('bolts', 123)
table.set_item('washers', 321)
table.set_item('lumber', 321)

table.print_table()
print(table.keys())