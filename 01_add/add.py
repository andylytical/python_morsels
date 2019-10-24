#import pprint

#def add( *a ):
#    rv = []
#    for by_index in zip( *a ):
#        inner_sums = [ sum(pieces)
#                       for pieces in zip( *by_index )
#                     ]
##        print( f"Inner part: '{inner_sums}'" )
#        rv.append( inner_sums )
##        print( f"ReturnVal (so far...): '{rv}'" )
##    pprint.pprint( rv )
#    return rv
#matrix1 = [[1, -2], [-3, 4]]
#matrix2 = [[2, -1], [0, -1]]
#add(matrix1, matrix2)
## [[3, -3], [-3, 3]]


def add( *a ):
    rv = [
            [
                sum(pieces)
                for pieces in zip( *by_index )
            ]
            for by_index in zip( *a )
         ]
    return rv
