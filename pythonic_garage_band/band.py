    
class Musician:
    def __init__(self, name = "empty", instrument = "empty", profession="empty", solo="empty"):
        self.name = name
        self.instrument = instrument
        self.profession = profession
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def __repr__(self):
        return f"{self.profession} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return self.solo

"""
    A class representing a musician.

    Member variables:
    - name (str): the name of the musician
    - instrument (str): the instrument played by the musician
    - profession (str): the profession of the musician
    - solo (str): the solo performed by the musician
    
    Methods:
    - get_instrument(): returns the instrument played by the musician
    - play_solo(): returns the solo performed by the musician
"""

class Guitarist(Musician):
    def __init__(self, name):
        instrument = "guitar"
        profession = "Guitarist"
        solo = "face melting guitar solo"
        super().__init__(name, instrument, profession, solo)
    
"""
    A class representing a guitarist.
    inherits from Musician class
"""

class Drummer(Musician):
    def __init__(self, name):
        instrument = "drums"
        profession = "Drummer"
        solo = "rattle boom crash"
        super().__init__(name, instrument, profession, solo)

"""
    A class representing a Drummer.
    inherits from Musician class
"""
    
class Bassist(Musician):
    def __init__(self, name):
        instrument = "bass"
        profession = "Bassist"
        solo = "bom bom buh bom"
        super().__init__(name, instrument, profession, solo)
    
"""
    A class representing a Bassist.
    inherits from Musician class
"""

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        get_solo = lambda member : member.play_solo()
        return list(map(get_solo, self.members))
    
    @staticmethod
    def to_list():
        return Band.instances

"""
    A class representing a band of Musicians.

    Member variables:
    - name (str): the name of the band
    - members (list): a list of Musician objects representing the members of the band
    
    Methods:
    - play_solos(): returns a list of solos performed by each member of the band
    - to_list(): returns a list of all Band objects that have been instantiated
"""