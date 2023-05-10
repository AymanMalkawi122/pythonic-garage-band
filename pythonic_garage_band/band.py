

        
class Musician:
    def __init__(self, name):
        self.name = name
    
class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
     
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    

class Band:
    def __init__(self, name,list):
        self.name=