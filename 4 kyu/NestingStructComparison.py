'''
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''


def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) == len(other):
            for orig_element, other_element in zip(original, other):
                if not same_structure_as(orig_element, other_element):
                    return False
        else:
            return False
    elif isinstance(original, list) or isinstance(other, list):
        return False
    else:
        return True

    return True
