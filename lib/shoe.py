#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand):
        self.brand = brand
        self.color = ''
        self.size = 0
        self.material = ''
        self.condition = 'Used'
        
    
    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
    def set_size(self, size):
        self.size = size
        
    def set_material(self, material):
        self.material = material
        
    def set_condition(self, condition):
        self.condition = condition
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    pass