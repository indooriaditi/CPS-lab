"""
CSCI-603: Lab1
Author: Aditi Indoori

This is a Sampler Quilt program that draws 
three different patchwork blocks of the same size.
This program demonstrates function reusability.
"""

import turtle as a
import math

a.setworldcoordinates(-500,-500,500,500)
a.speed(10)
a.title('Sampler Quilt')

def set_position() -> None:
  """
  Set the position to draw the first block
  :pre: (relative) pos (0,0), heading (west), down
  :post: (relative) pos (-100,0), heading (east), up
  :return: None
  """
  a.penup()
  a.backward(400)
  a.right(90)
  a.backward(200)
  a.left(90)
  a.pendown()

def border() -> None:
  """
  Draw the block border.
  :pre: (relative) pos (-100,0), heading (east), up
  :post: (relative) pos (0,0), heading (east), up
  :return: None
  """
  for i in range(4):
    for i in range(2):
      a.forward(200)
      a.right(90)
      a.forward(200 / 10)
      a.right(90)
    a.forward(200)
    a.right(90)
  
  # Set position to (0,0) facing east
  a.penup()
  a.right(45)
  a.forward(200 * math.sqrt(2) / 2)
  a.left(45)
  a.pendown()


def set_next() -> None:
  """
  Set the position to draw next block.
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (-100,0), heading (east), up
  :return: None
  """
  a.penup()
  a.left(45)
  a.forward(200 * math.sqrt(2) / 2)
  a.right(45)
  a.forward(50)
  a.pendown()


def large_triangle(large_triangle_leg, large_triangle_color, 
                   large_triangle_fill) -> None:
  """
  Draw large isoceles right triangle.
  Takes parameters for leg length and line/fill colors.
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (south west), up
  :return: None
  """
  a.color(large_triangle_color, large_triangle_fill)
  a.begin_fill()
  a.forward(large_triangle_leg * math.sqrt(2))
  a.left(135)
  a.forward(large_triangle_leg)
  a.left(90)
  a.forward(large_triangle_leg)
  a.end_fill()


def small_triangle(small_triangle_leg, small_triangle_color, 
                   small_triangle_fill) -> None:
  """
  Draw small isoceles right triangle.
  Takes parameters for leg length and line/fill colors.
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (south west), up
  :return: None
  """
  large_triangle(small_triangle_leg / math.sqrt(2), 
                 small_triangle_color, small_triangle_fill)


def square(square_side, square_color, square_fill) -> None:
  """
  Draw square.
  Takes parameters for side length and line/fill colors.
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (souh), up
  :return: None
  """
  a.color(square_color, square_fill)
  a.begin_fill()
  for i in range(4):
    a.forward(square_side)
    a.left(90)
  a.end_fill()


def rhombus(rhombus_side, rhombus_color, rhombus_fill) -> None:
  """
  Draw rhombus.
  Takes parameters for side length and line/fill colors.
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (east), up
  :return: None
  """
  a.color(rhombus_color, rhombus_fill)
  a.begin_fill()
  for i in range(2):
    a.forward(rhombus_side)
    a.left(45)
    a.forward(rhombus_side)
    a.left(135)
  a.end_fill()


def print1() -> None:
  """
  Draw first pattern inside the border.
  Calls large_triangle() and small_triangle()
  to draw a windmill like pattern.
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (east), up
  :return: None
  """
  for i in range(4):
    a.left(90)
    large_triangle(50, 'black', 'red')
    a.left(180)
    small_triangle(50, 'black', 'orange')
    a.left(90)


def print2() -> None:
  """
  Draw second pattern inside the border.
  Calls large_triangle() and square().
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (east), up
  :return: None
  """
  # Set position to draw the large triangle
  a.penup()
  a.left(45)
  a.forward(50 * math.sqrt(2) / 2)
  a.left(45)
  a.forward(50)
  a.left(135)
  a.pendown()

  # Draw the large triangles 
  # to intersect and form the pattern
  for i in range(4):
    large_triangle(50, 'black', 'red')
    a.backward(50)
    a.left(45)
    large_triangle(50, 'black', 'red')
    a.backward(100)
    a.right(45)

  # Fill in the colors by drawing squares
  # inside the triangle intersections
  a.forward(50 * math.sqrt(2) / 2)
  square(50 * math.sqrt(2), 'black', 'cyan')
  a.forward(50 * math.sqrt(2) / 2)
  a.left(45)
  square(50, 'black', 'blue')

  # Set position back to (0,0) facing east
  a.penup()
  a.left(45)
  a.forward(50 * math.sqrt(2) / 2)
  a.left(45)
  a.pendown()


def print3(length, color, fill1, fill2) -> None:
  """
  Draw third pattern inside the border
  :pre: (relative) pos (0,0), heading (east), up
  :post: (relative) pos (0,0), heading (east), up
  :return: None
  """
  # Draw inner rhombuses 
  for i in range(8):
    rhombus(length, color, fill1)
    a.left(45)
  a.end_fill()

  # Draw outer rhombuses
  for i in range(8):
    a.forward(length)
    a.right(45 / 2)
    rhombus(length / 2, color, fill2)
    a.left(45 / 2)
    a.backward(length)
    a.left(45)
  a.end_fill()

set_position()

# Display the first patchwork block
border()
print1()

# Set the position for next patchwork block
set_next()

# Display the second patchwork block
border()
print2()

# Set the position for next patchwork block
set_next()

# Display the third patchwork block
border()
print3(40, 'black', 'cyan', 'red')
print3(20, 'black', 'pink', 'yellow')

a.done()