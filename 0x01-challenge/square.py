#!/usr/bin/python3

""" Module for square class """

class Square():
    
    """ Represents a square.

    Returns:
        Width of the square
        Height of the square
    """
    
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):

        """ Instantiation of Class """

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):

        """ Calculates the area of the square """

        return self.width * self.height

    def perimeter_of_my_square(self):

        """ Calculates the perimeter of the square"""

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    """ Creates a square """

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
