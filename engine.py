values = {
    'r' : 1,
    'p' : 2,
    's' : 3
}

def compare( file1, file2, path ):

    actions1 = []
    actions2 = []

    f1 = path + file1 + '.py'
    f2 = path + file2 + '.py'

    print f1
    exec1 = {}
    execfile( f1, exec1 )
    f1 = exec1['rps']

    print f2
    exec2 = {}
    execfile( f2, exec2 )
    f2 = exec2['rps']


    for i in range(1000):

        value1 = f1( actions1, actions2 )
        value2 = f2( actions2, actions1 )

        print value1, '-', value2

        actions1.append( value1.lower() )
        actions2.append( value2.lower() )

    results = []

    for first, second in zip( actions1, actions2 ):

        result = values[ first ] - values[ second ]

        if result > 0:
            results.append( file1 )
        if result < 0:
            results.append( file2 )
        if result == 0:
            results.append( 'tie' )

    return results
