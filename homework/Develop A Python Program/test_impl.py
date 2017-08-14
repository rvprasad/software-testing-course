import impl
import pytest

NAME_PROP = "name"
FRIEND_PROP = "friend"

class TestNetwork:
    
    def setup_method(self, method):
        self.network = impl.Network()

    def teardown_method(self, method):
        self.network = None

    def test_create_person_succeeds(self):
        try:
            self.network.create_person()
        except:
            pytest.fail("create_person fails to create a person")

    def test_add_person_property_unique_string_name_for_existing_person(self):
        p1 = self.network.create_person()
        try:
            self.network.add_person_property(p1, NAME_PROP, "Jane")
        except:
            pytest.fail("add_person_property fails to associate a unique name to existing person")

    def test_add_person_property_overwrites_existing_property(self):
        p1 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        self.network.add_person_property(p1, ("owner", "House"), 25)
        try:
            self.network.add_person_property(p1, NAME_PROP, "Jan")
            self.network.add_person_property(p1, ("owner", "House"), 30)
        except:
            pytest.fail("add_person_property fails to overwrite existing property of an existing person")

    def test_add_person_property_same_person_with_same_name(self):
        p1 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        try:
            self.network.add_person_property(p1, NAME_PROP, "Jane")
        except:
            pytest.fail("add_person_property fails to name an existing person with the person's name")

    def test_add_person_property_non_string_name(self):
        p1 = self.network.create_person()
        with pytest.raises(TypeError, message="add_person_property does not fail when adding name property with non-string value"):
            self.network.add_person_property(p1, NAME_PROP, True)

    def test_add_person_property_different_persons_with_same_name(self):
        p1 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        p2 = self.network.create_person()
        with pytest.raises(ValueError, message="add_person_property does not fail when naming a person with an existing name"):
            self.network.add_person_property(p2, NAME_PROP, "Jane")

    def test_add_person_property_non_existent_person(self):
        with pytest.raises(RuntimeError, message="add_person_property does not fail when adding property to non-existing persons"):
            self.network.add_person_property(23, NAME_PROP, "Jane")

    def test_add_relation_existing_persons(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        try:
            self.network.add_relation(p1, p2)
        except:
            pytest.fail("add_relation fails to relate existing persons")

    def test_add_relation_non_existent_person1(self):
        p2 = self.network.create_person()
        with pytest.raises(RuntimeError, message="add_relation does not fail when adding relation between non-existent person and existing person"):
            self.network.add_relation("p1", p2)

    def test_add_relation_non_existent_person2(self):
        p1 = self.network.create_person()
        with pytest.raises(RuntimeError, message="add_relation does not fail when adding relation between existing person and non-existent person"):
            self.network.add_relation(p1, "p2")

    def test_add_relation_non_existent_persons(self):
        with pytest.raises(RuntimeError, message="add_relation does not fail when adding relation between non-existent persons"):
            self.network.add_relation("p1", "p2")
    
    def test_add_relation_existing_relation1(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        with pytest.raises(ValueError, message="add_relation does not fail when adding relation between related persons"):
            self.network.add_relation(p1, p2)

    def test_add_relation_existing_relation2(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        with pytest.raises(ValueError, message="add_relation does not fail when adding relation between related persons"):
            self.network.add_relation(p2, p1)

    def test_add_relation_property_existing_relation1(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p1, p2, ("married", "Manhattan"), 2010)

    def test_add_relation_property_existing_relation2(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p2, p1, ("married", "Manhattan"), 2010)

    def test_add_relation_property_overwrites_existing_property(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p1, p2, ("married", "Manhattan"), 2010)
        try:
            self.network.add_relation_property(p1, p2, ("married", "Manhattan"),
                    2015)
        except:
            pytest.fail("add_relation_property fails to overwrite existing property of an existing relation")

    def test_add_relation_property_overwrites_existing_property(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p1, p2, ("married", "Manhattan"), 2010)
        try:
            self.network.add_relation_property(p1, p2, ("married", "Manhattan"),
                    2015)
        except:
            pytest.fail("add_relation_property fails to overwrite existing property of an existing relation")

    def test_add_relation_property_boolean_friend_existing_relation(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        try:
            self.network.add_relation_property(p1, p2, FRIEND_PROP, True)
        except:
            pytest.fail("add_relation_property fails to associate boolean friend property to existing relation")

    def test_add_relation_property_non_boolean_friend(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        with pytest.raises(TypeError, message="add_relation_property does not fail when adding a non-boolean friend property to relation"):
            self.network.add_relation_property(p1, p2, FRIEND_PROP, "True")

    def test_add_relation_property_non_existent_relation(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        with pytest.raises(RuntimeError, message="add_relation_property does not fail when adding a property to non-existent relation"):
            self.network.add_relation_property(p1, p2, FRIEND_PROP, True)

    def test_get_person_existing_string_name(self):
        p1 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        assert p1 == self.network.get_person("Jane"), "get_person fails to get an existing person with given name"

    def test_get_person_non_existent_string_name(self):
        p1 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        with pytest.raises(RuntimeError, message="get_person does not fail for non-existent string names"):
            assert self.network.get_person("Jan")

    def test_get_person_non_string_name(self):
        p1 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        with pytest.raises(TypeError, message="get_person does not fail for non-string names"):
            assert self.network.get_person(True)

    def test_friends_of_friends_existing_string_name(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        p3 = self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "A")
        self.network.add_person_property(p2, NAME_PROP, "B")
        self.network.add_person_property(p3, NAME_PROP, "C")
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p1, p2, FRIEND_PROP, True)
        self.network.add_relation(p2, p3)
        self.network.add_relation_property(p2, p3, FRIEND_PROP, True)
        assert set([x for x in self.network.friends_of_friends("A")]) == set([p1, p3]), \
                "friends_of_friends fails to retrieve correct friends of friends of an existing person with existing name"

        p4 = self.network.create_person()
        self.network.add_person_property(p4, NAME_PROP, "D")
        assert not [x for x in self.network.friends_of_friends("D")], \
                "friends_of_friends fails to retrieve correct friends of friends of an existing person with existing name"
                
        p5 = self.network.create_person()
        self.network.add_person_property(p5, NAME_PROP, "E")
        self.network.add_relation(p4, p5)
        self.network.add_relation_property(p4, p5, FRIEND_PROP, True)
        assert set([x for x in self.network.friends_of_friends("D")]) == set([p4]), \
                "friends_of_friends fails to retrieve correct friends of friends of an existing person with existing name"

        self.network.add_relation(p3, p4)
        self.network.add_relation_property(p3, p4, FRIEND_PROP, True)
        assert set([x for x in self.network.friends_of_friends("A")]) == set([p1, p3]), \
                "friends_of_friends fails to retrieve correct friends of friends of an existing person with existing name"
        assert set([x for x in self.network.friends_of_friends("B")]) == set([p2, p4]), \
                "friends_of_friends fails to retrieve correct friends of friends of an existing person with existing name"

        self.network.add_relation_property(p3, p4, FRIEND_PROP, False)
        assert set([x for x in self.network.friends_of_friends("B")]) == set([p2]), \
                "friends_of_friends fails to retrieve correct friends of friends of an existing person with existing name"

    def test_friends_of_friends_non_existent_person(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p1, p2, FRIEND_PROP, True)
        with pytest.raises(RuntimeError, message="friends_of_friends does not fail for non-existent persons"):
            self.network.friends_of_friends("Tom")

    def test_friends_of_friends_non_string_name(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_relation_property(p1, p2, FRIEND_PROP, True)
        with pytest.raises(TypeError, message="friends_of_friends does not fail for non-string names"):
            self.network.friends_of_friends(24)

    def test_name_property_need_not_be_added(self):
        p1 = self.network.create_person()
        self.network.create_person()
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        assert p1 == self.network.get_person("Jane"), "Network implementation requires name as a mandatory property"

    def test_friend_property_need_not_be_provided(self):
        p1 = self.network.create_person()
        p2 = self.network.create_person()
        self.network.add_relation(p1, p2)
        self.network.add_person_property(p1, NAME_PROP, "Jane")
        assert not self.network.friends_of_friends("Jane"), "Network implementation requires friend as a mandatory property"
