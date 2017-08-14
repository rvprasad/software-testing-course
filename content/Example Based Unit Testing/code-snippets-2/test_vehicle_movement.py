# execute with
#   pytest -s test_vehicle_movement.py


import vehicle

class TestVehicleMovement:
    def setup_method(self):
        print("setup_method vehicle")
        self.vehicle = vehicle.Vehicle()
        self.vehicle.turn_engine_on()
        self.vehicle.set_capacity(4)
    
    def teardown_method(self):
        print("teardown_method vehicle")
        self.vehicle.turn_engine_off()
        self.vehicle = None
    
    def test_move(self):
        try:
            self.vehicle.accelerate_by(10)
        except:
            pytest.fail("accelerate_by should not have raised an exception")
        
    def test_move_turn_left(self):
        try:
            self.vehicle.accelerate_by(3)
            self.vehicle.travel(10)
            self.vehicle.turn_left()
            self.vehicle.travel(20)
        except BaseException as e:
            assert False, "none of the methods should have failed: " + str(e)
            

class TestCarMovement(TestVehicleMovement):
    def setup_method(self):
        print("setup_method car")
        self.vehicle = vehicle.Car()
        self.vehicle.set_num_wheels(3)
        self.vehicle.set_capacity(4)
        self.vehicle.turn_engine_on()
    

class TestTukTukMovement(TestVehicleMovement):
    def setup_method(self):
        print("setup_method tuktuk")
        self.vehicle = vehicle.TukTuk()
        self.vehicle.set_capacity(3)
        self.vehicle.set_num_wheels(3)
        self.vehicle.turn_engine_on()
    
