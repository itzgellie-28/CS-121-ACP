class DictionaryManager:
    def __init__(self):
        self.data = {}
    
    def add(self, key, value):
        self.data[key] = value  
    
    def get(self, key):
        if key in self.data:
            return self.data[key]
        return None
    
    def remove(self, key):
        if key in self.data:
            return self.data.pop(key)
        return None
    
    def is_empty(self):
        return len(self.data) == 0

manager = DictionaryManager()
manager.add("name", "Angel")
manager.add("age", 19)
manager.add("course", "IT")

print(f"Get name: {manager.get('name')}")
print(f"Removed age: {manager.remove('age')}")
