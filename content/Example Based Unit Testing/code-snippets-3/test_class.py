# execute 
#   pytest -s test_class.py


def setup_module():
    print("setting up MODULE 1")

def teardown_module():
    print("tearing down MODULE 1")


class TestClass1():

    def setup_method(self):
        print("    setting up TestClass1 INSTANCE")

    def teardown_method(self):
        print("    tearing down TestClass1 INSTANCE")

    def test_11(self):
        print("      test_11")
        pass

    def test_12(self):
        print("      test_12")
        pass

    @classmethod
    def setup_class(cls):
        print("  setting up TestClass1")
    
    @classmethod
    def teardown_class(cls):
        print("  tearing down TestClass1")


class TestClass2():

    def setup_method(self):
        print("    setting up TestClass2 INSTANCE")

    def teardown_method(self):
        print("    tearing down TestClass2 INSTANCE")

    def test_21(self):
        print("      test_21")
        pass

    def test_22(self):
        print("      test_22")
        pass

    @classmethod
    def setup_class(cls):
        print("  setting up TestClass2")
    
    @classmethod
    def teardown_class(cls):
        print("  tearing down TestClass2")


