def victory( opponent ):
    winning = {
        'r' : 'p',
        'p' : 's',
        's' : 'r'
    }

    return winning[ opponent ]


def choose():
    import random
    options = ['r', 'p', 's']
    return options[ random.randint( 0, 2 ) ]


def winner( me, opponent ):

    values = {
        'r' : 1,
        'p' : 2,
        's' : 3
    }

    result = values[ me ] - values[ opponent ]

    if result > 0:
        return 'me'

    if result < 0:
        return 'opponent'

    if result == 0:
        return 'tie'

def winners( me, opponent ):

    result = []

    for m, o in zip( me, opponent ):

        result.append( winner(m,o) )
