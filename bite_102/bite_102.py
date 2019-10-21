"""
Bite 102
"""
VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        user_input = input("enter a color ").lower()

        if user_input == "quit":
            print("bye")
            break
        
        if user_input not in VALID_COLORS:
            print("Not a valid color")
            continue
        else:
            print(user_input)