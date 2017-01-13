import random

options = ['r', 'p', 's']

def rps( my, other ):
    return options[ random.randint( 0, 2 ) ]
