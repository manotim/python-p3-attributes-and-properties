#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    # returns name when I access name through dot notation or an attr() function
    def get_name(self):
        return self._name
    # returns and SAVES changed name if condition is met
    def set_name(self, name):
        if isinstance(name, str) and (1<= len(name) <= 25):
        # if (type(name) in str) and (1<= len(name) <= 25): returns TypeError
            # assign incoming name as _name for Dog instance
            self._name = name.title()
        else:
            print('Name must be string between 1 and 25 characters.')
    # property() function compiles our getter and setter 
    # and calls them whenever anyone accesses dog's name
    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    breed = property(get_breed, set_breed)

