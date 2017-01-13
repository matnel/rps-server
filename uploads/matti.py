## returns the winner for an option
def winning( var ):

    if var == 'r':
        return 'p'

    if var == 'p':
        return 's'

    if var == 's':
        return 'r'

def rps( my, other ):

    if len( other ) == 0:
        return 'r'

    previous = other[-1]

    return winning( previous )
