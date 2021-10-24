#!/usr/bin/env python
# Copyright 2021 Samir Farhat Dominguez safarhat@bu.edu
# Copyright 2021 Fahad Farid fahadf@bu.edu
# ls -l

"""In this file I implement a Polynomial Class that performs multiple operations
and takes spacial issues into account."""

class Polynomial():
    """We try to Implement a Polynomial Class including all the necessary operations."""
    def __init__(self,sequence=None):
        self.array = {}
        if not sequence:
            return
        for i, item in enumerate(sequence):
            self.array[len(sequence)-1 - i] = item

    def __add__(self, value):
        summed = self.array.copy()
        for i in value.array.keys():
            summed[i] = self.array.get(i, 0) + value.array.get(i, 0)
        final = Polynomial()
        final.array = {k: summed[k] for k in sorted(summed, reverse=True)}
        return final

    def __sub__(self, value):

        summed = self.array.copy()
        for i in value.array.keys():
            summed[i] = self.array.get(i, 0) - value.array.get(i, 0)
        final = Polynomial()
        final.array = {k: summed[k] for k in sorted(summed, reverse=True)}
        return final

    def __mul__(self, value):
        calculated = {}

        array_keys = self.array.keys()
        value_keys = value.array.keys()

        if len(array_keys) >= len(value_keys):
            for i in array_keys:
                for j in value_keys:
                    calculated[i + j] = calculated.get(i + j, 0) + self.array[i] * value.array[j]
        else:
            for i in value_keys:
                for j in array_keys:
                    calculated[i + j] = calculated.get(i + j, 0) + self.array[j] * value.array[i]
        final = Polynomial()
        final.array = calculated
        return final

    def __eq__(self, value):
        if len(self.array) > len(value.array):
            for key in self.array.keys():
                if self.array.get(key, None) != value.array.get(key, None):
                    return False
        else:
            for key in value.array.keys():
                if self.array.get(key, None) != value.array.get(key, None):
                    return False
        return True


    def __getitem__(self, value):
        if value not in self.array.keys():
            return 0
        return self.array[value]

    def __setitem__(self, which, what):
        self.array[which] = what

    def deriv(self):
        """This function finds the Derivative of the Polynomial"""
        derivative = {}
        for key, value in self.array.items():
            if key == 0:
                continue
            derivative[key - 1] = key * value
        final = Polynomial()
        final.array = derivative
        return final

    def eval(self, num):
        """This function evaluates the Polynomial by replacing x values with the number given"""
        total = 0
        for key, value in self.array.items():
            total += value* (num ** key)
        return total
