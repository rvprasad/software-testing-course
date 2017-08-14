class Vehicle(object):
    
    def __init__(self):
        self.num_wheels = 0
        self.capacity = 0
        self.acceleration = 0
        self.started = False
    
    def set_num_wheels(self, num_wheels):
        self.num_wheels = num_wheels
        
    def set_capacity(self, capacity):
        self.capacity = capacity
        
    def turn_engine_on(self):
        self.started = True
        return
        
    def turn_engine_off(self):
        assert self.started
        return
        
    def accelerate_by(self, delta):
        assert self.started
        assert self.capacity > 0
        self.acceleration += delta
        return
        
    def turn_left(self):
        return
        
    def turn_right(self):
        return
        
    def travel(self, distance):
        assert self.started
        assert self.capacity > 0
        return
        

class Car(Vehicle):
    pass


class TukTuk(Vehicle):
    pass
