import math

def area_rect(length, width):
    """
    Calculates the area of a rectangle.
    If it's a square, uses length squared.
    """
    return length ** 2 if length == width else length * width

def area_circle(radius):
    """
    Calculates the area of a circle using pi *radius squared .
    """
    return math.pi * radius ** 2

def area_tri(base, height):
    """
    Calculates the area of a triangle using (1/2 * base * height).
    """
    return 0.5 * base * height