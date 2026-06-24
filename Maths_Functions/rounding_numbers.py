import math
# Measure Distance

# abs( value )
# returns the absolute (non-negative) value of a value.

print(abs(2 - 10))


# ------------------------------------------------------------------------------


# rounding Numbers


# round() :-
price = 35.549887
print(round(price))


# flooar()  :-
# floor() is not a built-in function, floor() belongs to the math module - import it before using
print(math.floor(price))


# ceil function
print(math.ceil(price))   # ceil function


# Trunc function
# Cuts off the decimal part and keeps the whole number (no rounding)

print(math.trunc(price))   # totally remove decimal part / no rounding  number



# extra round
# Round the number to the specified number of decimal places
print(round(price, 2))
