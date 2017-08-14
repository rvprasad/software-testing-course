# from correct_impl import FullCapacityError, Guest, Key, KeyCard, Lock, Hotel, \
#     Room
from impl import Guest, Key, KeyCard, Lock, Hotel, Room

try:
    from impl import FullCapacityError
except ImportError:
    class FullCapacityError(RuntimeError):
        pass


import re
import pytest
import unittest
import hypothesis.strategies as st
from hypothesis import assume, given

ENGLISH_ALPHABET_WITH_SPACE = \
    "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class TestKey(unittest.TestCase):
    def test_key_can_be_created(self):
        Key()


class TestKeyCard(unittest.TestCase):
    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()))
    def test_cannot_create_keycard_with_invalid_first_key_type(self, k1):
        with pytest.raises(ValueError):
            KeyCard(k1, Key())

    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()))
    def test_cannot_create_keycard_with_invalid_second_key_type(self, k2):
        with pytest.raises(ValueError):
            KeyCard(Key(), k2)

    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()),
           st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()))
    def test_cannot_create_keycard_with_invalid_key_types(self, k1, k2):
        with pytest.raises(ValueError):
            KeyCard(k1, k2)

    def test_can_create_keycard_with_distinct_valid_keys(self):
        KeyCard(Key(), Key())

    def test_can_create_keycard_with_same_valid_keys(self):
        tmp1 = Key()
        KeyCard(tmp1, tmp1)

    def test_first_key_returns_first_key(self):
        k1 = Key()
        k2 = Key()
        kc = KeyCard(k1, k2)
        assert kc.first_key == k1

    def test_second_key_returns_second_key(self):
        k1 = Key()
        k2 = Key()
        kc = KeyCard(k1, k2)
        assert kc.second_key == k2


class TestLock(unittest.TestCase):
    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
           st.none()))
    def test_cannot_create_lock_with_invalid_first_key_type(self, k1):
        with pytest.raises(ValueError):
            Lock(k1, Key())

    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
           st.none()))
    def test_cannot_create_lock_with_invalid_second_key_type(self, k2):
        with pytest.raises(ValueError):
            Lock(Key(), k2)

    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()),
           st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()))
    def test_cannot_create_lock_with_invalid_key_types(self, k1, k2):
        with pytest.raises(ValueError):
            Lock(k1, k2)

    def test_can_create_lock_with_distinct_valid_keys(self):
        Lock(Key(), Key())

    def test_can_create_lock_with_same_valid_keys(self):
        tmp1 = Key()
        Lock(tmp1, tmp1)

    @given(st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()))
    def test_cannot_unlock_with_invalid_keycard_type(self, value):
        key = Key()
        lock = Lock(key, key)
        with pytest.raises(ValueError):
            lock.can_be_unlocked(value)

    def test_can_unlock_with_matching_keycard(self):
        k1 = Key()
        k2 = Key()
        keycard = KeyCard(k1, k2)
        lock = Lock(k1, k2)
        assert lock.can_be_unlocked(keycard)

    def test_cannot_unlock_with_non_matching_keycard1(self):
        k1 = Key()
        k2 = Key()
        k3 = Key()
        k4 = Key()
        lock = Lock(k1, k2)
        keycard = KeyCard(k3, k4)
        assert not lock.can_be_unlocked(keycard)

    def test_cannot_unlock_with_non_matching_keycard2(self):
        k1 = Key()
        k2 = Key()
        k3 = Key()
        lock = Lock(k1, k2)
        keycard = KeyCard(k1, k3)
        assert not lock.can_be_unlocked(keycard)

    def test_cannot_unlock_with_non_matching_keycard3(self):
        k1 = Key()
        k2 = Key()
        k3 = Key()
        lock = Lock(k1, k2)
        keycard = KeyCard(k3, k2)
        assert not lock.can_be_unlocked(keycard)

    def test_cannot_unlock_with_non_matching_keycard4(self):
        k1 = Key()
        k2 = Key()
        k3 = Key()
        lock = Lock(k1, k2)
        keycard = KeyCard(k3, k1)
        assert not lock.can_be_unlocked(keycard)

    def test_can_unlock_with_partially_matching_keycard(self):
        k1 = Key()
        k2 = Key()
        k3 = Key()
        lock = Lock(k1, k2)
        keycard1 = KeyCard(k2, k3)
        # can unlock with partial match
        assert lock.can_be_unlocked(keycard1)
        keycard2 = KeyCard(k2, k1)
        # cannot unlock with partial match
        assert not lock.can_be_unlocked(keycard2)


class TestRoom(unittest.TestCase):
    @given(st.one_of(st.text(), st.floats(), st.booleans(), st.none()))
    def test_cannot_create_room_with_invalid_room_number_type(self, num):
        with pytest.raises(ValueError):
            Room(num, Lock(Key(), Key()))

    @given(st.one_of(st.text(), st.integers(), st.floats(),
                     st.booleans(), st.none()))
    def test_cannot_create_room_with_invalid_lock_type(self, lock):
        with pytest.raises(ValueError):
            Room(1, lock)

    @given(st.integers(max_value=0))
    def test_cannot_create_room_with_invalid_room_number(self, num):
        with pytest.raises(ValueError):
            Room(num, Lock(Key(), Key()))

    @given(st.integers(min_value=1))
    def test_can_create_room_with_valid_room_number_and_lock(self, num):
        Room(num, Lock(Key(), Key()))

    @given(st.integers(min_value=1))
    def test_room_number_returns_initialized_room_number(self, num):
        assert Room(num, Lock(Key(), Key())).room_number == num

    @given(st.integers(min_value=1))
    def test_lock_returns_initialized_lock(self, num):
        lock = Lock(Key(), Key())
        assert Room(num, lock).lock == lock


class TestGuest(unittest.TestCase):
    @given(st.one_of(st.text(), st.floats(), st.booleans(), st.none()))
    def test_cannot_create_guest_with_invalid_room_number_type(self, num):
        with pytest.raises(ValueError):
            Guest("John", num, KeyCard(Key(), Key()))

    @given(st.one_of(st.integers(), st.floats(), st.booleans(), st.none()))
    def test_cannot_create_guest_with_invalid_name_type(self, name):
        with pytest.raises(ValueError):
            Guest(name, 1, KeyCard(Key(), Key()))

    @given(st.one_of(st.integers(), st.floats(), st.booleans(), st.none()))
    def test_cannot_create_guest_with_invalid_keycard_type(self, kc):
        with pytest.raises(ValueError):
            Guest("John", 1, kc)

    @given(st.integers(max_value=0))
    def test_cannot_create_guest_with_invalid_room_number(self, num):
        with pytest.raises(ValueError):
            Guest("John", num, KeyCard(Key(), Key()))

    @given(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, max_size=1),
           st.integers(min_value=1))
    def test_cannot_create_guest_with_invalid_name1(self, name, num):
        with pytest.raises(ValueError):
            Guest(name, num, KeyCard(Key(), Key()))

    @given(st.text(min_size=2), st.integers(min_value=1))
    def test_cannot_create_guest_with_invalid_name2(self, name, num):
        assume(re.sub(r'[a-zA-Z ]', '', name))
        with pytest.raises(ValueError):
            Guest(name, num, KeyCard(Key(), Key()))

    @given(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
           st.integers(min_value=1))
    def test_can_create_guest_with_valid_arguments(self, name, num):
        Guest(name, num, KeyCard(Key(), Key()))

    @given(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
           st.integers(min_value=1))
    def test_guest_name_returns_initialized_name(self, name, num):
        assert Guest(name, num, KeyCard(Key(), Key())).guest_name == name

    @given(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
           st.integers(min_value=1))
    def test_room_number_returns_initialized_room_number(self, name, num):
        assert Guest(name, num, KeyCard(Key(), Key())).room_number == num

    @given(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
           st.integers(min_value=1))
    def test_keycard_returns_initialized_keycard(self, name, num):
        kc = KeyCard(Key(), Key())
        assert Guest(name, num, kc).keycard == kc

    @given(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
           st.integers(min_value=1),
           st.one_of(st.text(), st.integers(), st.floats(), st.booleans(),
                     st.none()))
    def test_is_checkedin_fails_with_invalid_hotel_type(self, name, num,
                                                        value):
        kc = KeyCard(Key(), Key())
        g = Guest(name, num, kc)
        with pytest.raises(ValueError):
            g.is_checkedin(value)

    def test_is_checkedin_returns_true_when_checkedin(self):
        hotel = Hotel(10)
        guest = hotel.checkin("John")
        assert guest.is_checkedin(hotel)

    def test_is_checkedin_returns_false_when_not_checkedin(self):
        hotel = Hotel(10)
        guest = hotel.checkin("John")
        hotel.checkout("John")
        assert not guest.is_checkedin(hotel)


class TestHotel(unittest.TestCase):

    NUM_OF_GUESTS = 25

    @given(st.integers(max_value=9))
    def test_cannot_create_hotel_with_invalid_number_of_rooms1(self, n):
        with pytest.raises(Exception):
            Hotel(n)

    @given(st.integers(min_value=1001))
    def test_cannot_create_hotel_with_invalid_number_of_rooms2(self, n):
        with pytest.raises(Exception):
            Hotel(n)

    @given(st.integers(min_value=10, max_value=1000))
    def test_valid_hotel_creation(self, n):
        Hotel(n)

    @given(st.integers(min_value=10, max_value=1000),
           st.one_of(st.integers(), st.floats(), st.booleans(), st.none()))
    def test_checkin_fails_with_invalid_guest_name_type(self, n, name):
        h = Hotel(n)
        with pytest.raises(ValueError):
            h.checkin(name)

    @given(st.integers(min_value=10, max_value=1000),
           st.one_of(st.integers(), st.floats(), st.booleans(), st.none()))
    def test_is_checkedin_fails_with_invalid_guest_name_type(self, n, name):
        h = Hotel(n)
        with pytest.raises(ValueError):
            h.is_checkedin(name)

    @given(st.integers(min_value=10, max_value=1000),
           st.one_of(st.integers(), st.floats(), st.booleans(), st.none()))
    def test_room_of_fails_with_invalid_guest_name_type(self, n, name):
        h = Hotel(n)
        with pytest.raises(ValueError):
            h.room_of(name)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_after_checkin_guest_has_been_assigned_room1(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        guests = []
        for n in names:
            guests.append(hotel.checkin(n))
        for g in guests:
            assert hotel.room_of(g.guest_name).room_number == g.room_number

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_after_checkin_guest_has_been_assigned_room2(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        guests = []
        for n in names:
            guests.append(hotel.checkin(n))
        for g in guests:
            assert isinstance(hotel.room_of(g.guest_name), Room)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_after_checkin_guest_appear_as_checkedin(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        for n in names:
            hotel.checkin(n)
        for n in names:
            assert hotel.is_checkedin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_checkout_of_checkedin_guest(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        for n in names:
            hotel.checkin(n)
        for n in names:
            hotel.checkout(n)
        for n in names:
            assert not hotel.is_checkedin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_checkout_of_not_checkedin_guest(self, names1, names2, num):
        assume(len(names1) < num)
        assume(not (names1 & names2))
        hotel = Hotel(num)
        for n in names1:
            hotel.checkin(n)
        for n in names2:
            hotel.checkout(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_after_checkout_guest_appears_checkedout(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        for n in names:
            hotel.checkin(n)
        for n in names:
            hotel.checkout(n)
            assert not hotel.is_checkedin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_after_checkout_guest_doesnot_have_room(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        for n in names:
            hotel.checkin(n)
        for n in names:
            hotel.checkout(n)
            with pytest.raises(ValueError):
                assert hotel.room_of(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=1),
           st.integers(min_value=10, max_value=1000))
    def test_checkedin_guest_has_a_room(self, names1, names2, num):
        assume(len(names1) < num)
        assume(names1 & names2)
        hotel = Hotel(num)
        for n in names1:
            hotel.checkin(n)
        for n in names2:
            if hotel.is_checkedin(n):
                assert isinstance(hotel.room_of(n), Room)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=1, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_guest_having_a_room_is_checkedin(self, names1, names2, num):
        assume(len(names1) < num)
        assume(names1 & names2)
        hotel = Hotel(num)
        for n in names1:
            hotel.checkin(n)
        for n in names2:
            try:
                if isinstance(hotel.room_of(n), Room):
                    assert hotel.is_checkedin(n)
            except ValueError:
                pass

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=10, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_checkins_beyond_capacity_will_not_occur(self, names, num):
        assume(len(names) > num)
        hotel = Hotel(num)
        names = list(names)
        for n in names[0:num]:
            hotel.checkin(n)
        for n in names[num:]:
            with pytest.raises(FullCapacityError):
                hotel.checkin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_guests_with_unique_name_can_be_checkedin(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        for n in names:
            hotel.checkin(n)
        for n in names:
            hotel.checkout(n)
        for n in names:
            hotel.checkin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_two_guests_with_same_name_cannot_be_checkedin(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        for n in names:
            hotel.checkin(n)
        for n in names:
            with pytest.raises(ValueError):
                hotel.checkin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_two_checkedin_guests_are_not_assigned_the_same_room_number(
            self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        guests = []
        for n in names:
            guests.append(hotel.checkin(n))
        for g1 in guests:
            for g2 in guests:
                assert g1 == g2 or g1.room_number != g2.room_number

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_two_checkedin_guests_are_not_assigned_the_same_room1(
            self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        guests = []
        for n in names:
            guests.append(hotel.checkin(n))
        for g1 in guests:
            for g2 in guests:
                assert g1 == g2 or \
                    hotel.room_of(g1.guest_name) != hotel.room_of(g2.guest_name)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2),
           st.integers(min_value=10, max_value=1000))
    def test_two_checkedin_guests_are_not_assigned_the_same_room2(
            self, names1, names2, num):
        assume(len(names2 | names1) <= num)
        assume(names1 & names2)
        hotel = Hotel(num)
        name2guest = {}
        for n in names1:
            name2guest[n] = hotel.checkin(n)
        for n1 in names2:
            if n1 in names1:
                hotel.checkout(n1)
                name2guest.pop(n1)
            else:
                g1 = hotel.checkin(n1)
                for n2 in name2guest:
                    assert name2guest[n2].room_number != \
                        g1.room_number
                    assert hotel.room_of(n2) != \
                        hotel.room_of(g1.guest_name)
                name2guest[n1] = g1

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2, max_size=NUM_OF_GUESTS),
           st.integers(min_value=10, max_value=1000))
    def test_checkin_is_possible_if_hotel_is_not_full(self, names, num):
        assume(len(names) < num)
        h = Hotel(num)
        for n in names:
            h.checkin(n)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2),
           st.integers(min_value=10, max_value=1000))
    def test_every_room_in_a_hotel_has_unique_lock(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        locks = set()
        for n in names:
            hotel.checkin(n)
            lock = hotel.room_of(n).lock
            assert lock not in locks
            locks.add(lock)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=2),
           st.integers(min_value=10, max_value=1000))
    def test_every_guest_in_a_hotel_has_unique_keycard(self, names, num):
        assume(len(names) < num)
        hotel = Hotel(num)
        keycards = set()
        for n in names:
            g = hotel.checkin(n)
            kc = g.keycard
            assert kc not in keycards
            keycards.add(kc)

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=10),
           st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=1),
           st.integers(min_value=10, max_value=1000))
    def test_assigned_room_cannot_be_opened_with_old_keycard(
            self, names1, names2, num):
        assume(len(names1) == num)
        assume(not names1 & names2)
        hotel = Hotel(num)
        room2keycard = {}
        for n in names1:
            g = hotel.checkin(n)
            room2keycard[g.room_number] = g.keycard
            # without this line, unused keycard can render the lock
            # unlockable to subsequent keycards
            hotel.room_of(n).lock.can_be_unlocked(g.keycard)
        for n1, n2 in zip(names1, names2):
            hotel.checkout(n1)
            g = hotel.checkin(n2)
            room = hotel.room_of(n2)
            assert room.lock.can_be_unlocked(g.keycard)
            assert not room.lock.can_be_unlocked(room2keycard[room.room_number])
            room2keycard[g.room_number] = g.keycard

    @given(st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=10),
           st.sets(st.text(alphabet=ENGLISH_ALPHABET_WITH_SPACE, min_size=2),
                   min_size=1),
           st.integers(min_value=10, max_value=1000))
    def test_first_key_of_keycard_is_same_as_the_second_key_of_previous_card(
            self, names1, names2, num):
        assume(len(names1) == num)
        assume(not names1 & names2)
        hotel = Hotel(num)
        room2keycard = {}
        for n in names1:
            g = hotel.checkin(n)
            room2keycard[g.room_number] = g.keycard
        for n1, n2 in zip(names1, names2):
            hotel.checkout(n1)
            g = hotel.checkin(n2)
            assert g.keycard.first_key == \
                room2keycard[hotel.room_of(g.guest_name).room_number].second_key
