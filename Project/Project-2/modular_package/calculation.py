import math


def factorial(number):
    return math.factorial(number)


def compound_interest(principal, rate ,years):
    amount = principal * (1 + rate / 100) ** years
    return amount


def trigonometric(angle_degrees):
    radians = math.radians(angle)

    sin = math.sin(radians)
    cos = math.cos(radians)
    tan = math.tan(radians)

    return sin, cos, tan


def circle_area(radius):
    return math.pi*radius*radius


def rectangle_area(length,width):
    return length*width
