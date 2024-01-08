"""
CSCI-603 Lab 3: Islands

A program that draws fractal islands in a 
turtle's canvas using recursion.

The program draws fractal islands using 
two different fractal curves.

author: ADITI INDOORI
"""

import math
import re
import turtle as a


def fractal_curve_1(side_length: int, level: int, total_length: int) -> int:
    """
    Draw the first fractal curve.
    :args:
        side_length (int): the length to move forward
        level (int): the number of levels of recursive calls made
        total_length (int): perimeter of the curve
    :return: 
        int: total perimeter length for the curve
    """
    
    # the first level draws a straight line of length side_length
    if level == 1:
        a.forward(side_length)
        total_length += side_length
    
    # every other level is drawn using recursive calls 
    # to draw side with the level one less
    else:
        total_length = fractal_curve_1(side_length/3, level-1, total_length)
        a.right(60)
        total_length = fractal_curve_1(side_length/3, level-1, total_length)
        a.left(120)
        total_length = fractal_curve_1(side_length/3, level-1, total_length)
        a.right(60)
        total_length = fractal_curve_1(side_length/3, level-1, total_length)
    return total_length


def fractal_curve_2(side_length: int, level: int, total_length: int) -> int:
    """
    Draw the second fractal curve.
    :args:
        side_length (int): the length to move forward
        level (int): the number of levels of recursive calls made
        total_length (int): perimeter of the curve
    :return: 
        int: total perimeter length for the curve
    """
    
    # the first level draws a straight line of length side_length
    if level == 1:
        a.forward(side_length)
        total_length += side_length
    
    # every other level is drawn using recursive calls 
    # to draw side with the level one less
    else:
        a.right(45)
        total_length = fractal_curve_2(side_length/math.sqrt(2), level-1, total_length)
        a.left(90)
        total_length = fractal_curve_2(side_length/math.sqrt(2), level-1, total_length)
        a.right(45)
    return total_length


def main() -> None:
    """
    The main logic to draw the islands.
    :return: 
        None
    """
    
    # taking input from user for number of sides
    # and validating whether it is of type int
    side_temp = input('Number of sides: ')
    while (not re.fullmatch(r'[0-9]+', side_temp)):
        print("Value must be a type int. You entered 'string-value'.")
        side_temp = input('Number of sides: ')
    else:
        side = int(side_temp)
        
    # taking input from user for length of side
    # and validating whether it is of type float
    length_temp = input('Length of initial side: ')
    while (not (re.fullmatch(r'[0-9]+\.[0-9]+', length_temp) 
                or re.fullmatch(r'[0-9]+', length_temp))):
        print("Value must be a type float. You entered 'string-value'.")
        length_temp = input('Length of initial side: ')
    else:
        length = float(length_temp)
    
    # taking input from user for number of levels
    # and validating whether it is of type int
    level_temp = input('Number of levels: ')
    while (not re.fullmatch(r'[0-9]+', level_temp)):
        print("Value must be a type int. You entered 'string-value'.")
        level_temp = input('Number of levels: ')
    else:
        level = int(level_temp)

    #a.tracer(0, 0)
    
    # setting perimeter of first island to 0 initially
    total_perimeter_1 = 0

    # setting the position to draw the island in anti-clockwise direction
    a.left(180)
    
    # iterating through the numer of sides and calling the 
    # fractal_curve_1 function to draw the curve for each side
    # and adding the length of each side to the total perimeter of the island
    for i in range(side):
        a.right(360 / side)
        total_perimeter_1 += fractal_curve_1(length, level, 0)
    print("Curve 1 - Island's length is " + str(total_perimeter_1) + " units.")

    enter_to_continue = input("Hit enter to continue...")

    # resetting the canvas before drawing second island 
    a.reset()

    # setting perimeter of first island to 0 initially
    total_perimeter_2 = 0
    
    # setting the position to draw the island in anti-clockwise direction
    a.left(180)
    
    # iterating through the numer of sides and calling the 
    # fractal_curve_2 function to draw the curve for each side
    # and adding the length of each side to the total perimeter of the island
    for i in range(side):
        a.right(360/side)
        total_perimeter_2 += fractal_curve_2(length, level, 0)
    print("Curve 2 - Island's length is " + str(total_perimeter_2) + " units.")
    print('Bye!')

    #a.update()
    a.done()


if __name__ == '__main__':
    main()
