"""
Bite 42: Number Guessing Game Class

In this Bite you implement a Game class to perform a number guessing game. 
It lets a user do a max of 5 guesses of a secret number between 1 and 20 randomly defined by the class.

Note you have to account for invalid inputs: raise a ValueError if a user hits Enter (nothing entered), 
a non-numeric value, a number that is not in the 1-20 range, or guesses the same number again. 
See the template code below ... (Advanced Bite, not giving away too much!)

The tests run through a lose scenario as well. 
Note they mock out the input builtin to test this. 
And you will be tested on stdout too so use print statements in addition to return values.
 Here is how the program would work from the command line.

Good luck, have fun and keep calm and code in Python!
"""
import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""
    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self) -> int:
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int
        """
        message = f"Guess a number between {START} and {END}: "
        user_input = ""

        user_input = input(message)

        # empty
        if not user_input:
            raise ValueError("Please enter a number")
        else:
            try:
                s_to_i = int(user_input)
            except ValueError:
                raise ValueError("Should be a number")
            # ok
            ## already guessed
            # not in range
            if s_to_i >= START and s_to_i <= END:
                if s_to_i in self._guesses:
                    raise ValueError("Already guessed")
                else:
                    self._guesses |= {s_to_i}
                    return s_to_i
            else:
                raise ValueError("Number not in range")

    def _validate_guess(self, guess) -> bool:
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True

        if guess > self._answer:
            print(f"{guess} is too high")
        elif guess < self._answer:
            print(f"{guess} is too low")

        return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        tryes = 0

        while tryes < MAX_GUESSES:
            try:
                user_guess = self.guess()
            except ValueError as err:
                print(err)
                continue

            ok = self._validate_guess(user_guess)
            if ok:
                tryes += 1
                self._win = True
                break
            tryes += 1

        if self._win:
            print(f"It took you {tryes} guesses")
        else:
            print(f"Guessed 5 times, answer was {self._answer}")

