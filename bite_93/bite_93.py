"""
Bite 93. Rock-paper-scissors and generator's send
"""
from random import choice

defeated_by = dict(paper='scissors', rock='paper', scissors='rock')

lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move() -> str:
    """Randomly select a move"""
    return choice([key for key in defeated_by.keys()])


def _get_winner(computer_choice, player_choice) -> str:
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    result = defeated_by.get(player_choice, None)

    if not result:
        return 'Invalid'

    if computer_choice == player_choice:
        return tie

    if result == computer_choice:
        return lose.format(computer_choice, player_choice)

    return win.format(player_choice, computer_choice)


def game_loop():
    start = True
    get_result = None
    while True:
        get_result = yield

        if start:
            print('Welcome to Rock Paper Scissors')
            start = False
        else:
            if get_result:
                if get_result == 'q':
                    raise StopIteration

                com_move = _get_computer_move()
                user_move = get_result

                print(_get_winner(com_move, user_move))


def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    gen = game_loop()
    gen.send(None)
    return gen
