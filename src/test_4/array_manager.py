class ArrayManager:
    def __init__(self, array):
        self.array = array
    
    def add_element(self, element):
        self.array.append(element)

    def remove_element(self, element):
        self.array.remove(element)
    
    def find_element(self, element):
        return element in self.array

    def sum_elements(self):
        return sum(self.array)
    
    def max_element(self):
        return max(self.array)
    
    def min_element(self):
        return min(self.array)

    def sort_ascending(self):
        self.array.sort()
    
    def sort_descending(self):
        self.array.sort(reverse=True)

    def clear(self):
        self.array = []