"""A simple lottery  Python."""

import random

PLARYER = ('Jane', 'Paul', 'James')

def winner(people=PLAYER):
    """Choose a winner at random from the given list of player."""
    x = random.randrange(0,len(player))
    return player[x]

# The if statement below is only true if we are calling this file as a script.
if __name__ == '__main__':
    print '... and the winner is!'
    your_input = raw_input()
    print winner(PLARYER)