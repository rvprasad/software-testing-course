class Key(object):
    "Key used in keycards and locks"
    
    pass


class KeyCard(object):
    "Keycard used to open a lock"

    def __init__(self, first_key, second_key):
        "Constructs a KeyCard with the given keys"
        pass

    @property
    def first_key(self):
        "Provides the first key of this keycard"
        pass

    @property
    def second_key(self):
        "Provides the second key of this keycard"
        pass


class Lock(object):
    "Lock on a room door"

    def __init__(self, first_key, second_key):
        "Constructs a Lock with the given keys"
        pass

    def can_be_unlocked(self, keycard):
        """
        Checks if this lock can be unlocked with the given keycard
        
        Return:
            True if the lock can be unlocked; False otherwise
        """
        pass


class Room(object):
    "Room in a hotel"

    def __init__(self, room_number, lock):
        "Constructs a Room with given number and lock"
        pass

    @property
    def room_number(self):
        "Provides the number of this room"
        pass

    @property
    def lock(self):
        "Provides the lock for this room"
        pass


class Guest(object):
    "Guest at a hotel"
    def __init__(self, guest_name, room_number, keycard):
        pass

    @property
    def guest_name(self):
        "Provides the name of this guest"
        pass

    @property
    def keycard(self):
        "Provides the keycard of this guest"
        pass

    @property
    def room_number(self):
        "Provides the number of the room occupied by this guest"
        pass

    def is_checkedin(self, hotel):
        "Checks if this guest is checked into this hotel"
        pass


class Hotel(object):
    "Hotel"
    
    def __init__(self, N):
        "Constructs a Hotel with N rooms"
        pass

    def checkin(self, guest_name):
        """
        Checks the guest into the hotel by allocating a room
        
        Return:
            the corresponding Guest
        """
        pass

    def is_checkedin(self, guest_name):
        """
        Checks if the guest is a guest at this Hotel
        
        Return:
            True if the guest is checked in at this Hotel; False otherwise
        """
        pass

    def checkout(self, guest_name):
        "Checks out the guest from the hotel"
        pass

    def room_of(self, guest_name):
        """
        Provides the room for the guest
        
        Return:
            the corresponding Room
        """
        pass


