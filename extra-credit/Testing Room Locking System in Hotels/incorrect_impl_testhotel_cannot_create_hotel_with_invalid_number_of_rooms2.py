import re


class Key(object):
    "Key used in keycards and locks"
    pass


class KeyCard(object):
    "Keycard used to open a lock"

    def __init__(self, first_key, second_key):
        """
        Constructs a KeyCard with the given keys

        Args:
            first_key: in the keycard to be created
            second_key: in the keycard to be created

        Raises:
            ValueError if any of the keys are not of type Key
        """
        if not isinstance(first_key, Key):
            raise ValueError("First key is not of Key type")
        if not isinstance(second_key, Key):
            raise ValueError("Second key is not of Key type")
        self._keys = (first_key, second_key)

    @property
    def first_key(self):
        "Provides the first key of this keycard"
        return self._keys[0]

    @property
    def second_key(self):
        "Provides the second key of this keycard"
        return self._keys[1]


class Lock(object):
    "Lock on a room door"

    def __init__(self, first_key, second_key):
        """
        Constructs a Lock with the given keys

        Args:
            first_key: in the lock to be created
            second_key: in the lock to be created

        Raises:
            ValueError if any of the keys are not of type Key
        """
        if not isinstance(first_key, Key):
            raise ValueError("First key is not of Key type")
        if not isinstance(second_key, Key):
            raise ValueError("Second key is not of Key type")

        self._keys = (first_key, second_key)

    def can_be_unlocked(self, keycard):
        """
        Checks if this lock can be unlocked with the given keycard

        Return:
            True if the lock can be unlocked; False otherwise

        Raises:
            ValueError if keycard is not of KeyCard Type
        """
        if not isinstance(keycard, KeyCard):
            raise ValueError("keycard is not of KeyCard type")
        if self._keys[0] == keycard.first_key and \
                self._keys[1] == keycard.second_key:
            return True
        elif self._keys[1] == keycard.first_key:
            self._keys = (keycard.first_key, keycard.second_key)
            return True
        else:
            return False


class Room(object):
    "Room in a hotel"

    def __init__(self, room_number, lock):
        """
        Constructs a Room with given number and lock

        Args:
            room_number: of this room.  This has be to greater than 0.
            lock: of this room.

        Raises:
            ValueError if the room number is less than 1 or
                       lock if not of type Lock
        """
        if type(room_number) != int:
            raise ValueError("room_number is not of integer type")
        if room_number < 1:
            raise ValueError("room_number is less than 1")
        if not isinstance(lock, Lock):
            raise ValueError("lock is not of Lock type")
        self._number = room_number
        self._lock = lock

    @property
    def last_key(self):
        return self._last_key

    @last_key.setter
    def last_key(self, key):
        self._last_key = key

    @property
    def keys(self):
        k = self.last_key
        self.last_key = Key()
        return (k, self.last_key)

    @property
    def room_number(self):
        "Provides the number of this room"
        return self._number

    @property
    def lock(self):
        "Provides the lock for this room"
        return self._lock


class Guest(object):
    "Guest at a hotel"
    def __init__(self, name, room_number, keycard):
        """
        Constructs a Guest in given room number and with given keycard

        Args:
            name: of the guest.  This should be at least 2 characters long and
                  be composed of letters from English alphabet.
            room_number: of room allocated to the guest
            keycard: provided to this guest to unlock the allocated room

        Raises:
            ValueError if name is ill-formed or room number is less than 1
        """
        if type(room_number) != int:
            raise ValueError("room_number is not of integer type")
        if room_number < 1:
            raise ValueError("room_number is less than 1")
        if not isinstance(name, str):
            raise ValueError("name is not of string type")
        if len(name) < 2:
            raise ValueError("name is less than 2 characters long")
        if re.search(r'[^a-zA-Z ]', name) is not None:
            raise ValueError("name contain characters not in English alphabet")
        if not isinstance(keycard, KeyCard):
            raise ValueError("keycard is not of KeyCard type")
        self._guest_name = name
        self._room_number = room_number
        self._keycard = keycard

    @property
    def guest_name(self):
        "Provides the name of this guest"
        return self._guest_name

    @property
    def keycard(self):
        "Provides the keycard of this guest"
        return self._keycard

    @property
    def room_number(self):
        "Provides the number of the room occupied by this guest"
        return self._room_number

    def is_checkedin(self, hotel):
        """
        Checks if this guest is checked into this hotel

        Returns:
            True if this guest is checked in at the given hotel;
            False otherwise

        Raises:
            ValueError if hotel is not of Hotel type
        """
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel is not of Hotel type")
        return hotel.is_checkedin(self._guest_name)


class FullCapacityError(RuntimeError):
    pass


class Hotel(object):
    "Hotel"

    def __init__(self, N):
        "Constructs a Hotel with N rooms"
        if type(N) != int:
            raise ValueError("N is not of int type")
        if N < 10:
            raise ValueError("N is not between 10 and 1000, both inclusive")
        self._name2guest = {}
        self._name2room = {}
        self._capacity = N
        self._empty_rooms = []
        for i in range(1, N + 1):
            k = Key()
            r = Room(i, Lock(k, k))
            r.last_key = k
            self._empty_rooms.append(r)

    def checkin(self, guest_name):
        """
        Checks the guest into the hotel by allocating a room

        Return:
            the corresponding Guest

        Raises:
            ValueError if guest name is not of str type or
                       is already checked in at this hotel
        """
        if not isinstance(guest_name, str):
            raise ValueError("guest name is not of string type")
        if guest_name in self._name2guest:
            raise ValueError(
                "guest named {0} is already checked in".format(guest_name))
        if len(self._name2guest) >= self._capacity:
            raise FullCapacityError()
        room = self._empty_rooms.pop()
        last_key, new_key = room.keys
        guest = Guest(guest_name, room.room_number, KeyCard(last_key, new_key))
        self._name2guest[guest_name] = guest
        self._name2room[guest_name] = room
        return guest

    def is_checkedin(self, guest_name):
        """
        Checks if the guest is a guest at this Hotel

        Return:
            True if the guest is checked in at this Hotel; False otherwise

        Raises:
            ValueError if guest name is not of str type
        """
        if not isinstance(guest_name, str):
            raise ValueError("guest name is not of string type")
        return guest_name in self._name2guest

    def checkout(self, guest_name):
        """
        Checks out the guest from the hotel

        Raises:
            ValueError if guest name is not of str type
        """
        if not isinstance(guest_name, str):
            raise ValueError("guest name is not of string type")
        if guest_name in self._name2guest:
            del self._name2guest[guest_name]
            room = self._name2room.pop(guest_name)
            self._empty_rooms.append(room)

    def room_of(self, guest_name):
        """
        Provides the room for the guest

        Return:
            the corresponding Room

        Raises:
            ValueError if named guest is not a string or
                       is not checked in at this hotel
        """
        if not isinstance(guest_name, str):
            raise ValueError("guest name is not of string type")
        if guest_name not in self._name2room:
            raise ValueError(
                "guest {0} is not checked in at this  hotel".format(guest_name))
        return self._name2room[guest_name]
