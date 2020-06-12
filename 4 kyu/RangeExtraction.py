'''
A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''

def solution(args):
    sol = [] # List of integers converted to strings, will join before returning
    consecutives = [args[0]] # KEeps track of consecutive numbers

    # Sort list
    args.sort()
    
    # Loop through range(1, len(args))
    # Check backwards for consecutives -- that is if args[n] == args[n-1] + 1
    # This is to avoid dealing with errors involving going out of bounds
    # If n is a consecutive number, append to consecutives
    for n in range(1, len(args)):
        if args[n] != args[n-1]+1: # If not consecutive
            if len(consecutives) == 1:
                sol.append(str(consecutives[0]))
                consecutives.clear()

            elif len(consecutives) == 2:
                sol.append(str(consecutives[0]))
                sol.append(str(consecutives[1]))
                consecutives.clear()

            else: # Must be a valid range (3 or more consecutive values)
                range_str = f'{consecutives[0]}-{consecutives[-1]}'
                sol.append(range_str)
                consecutives.clear()

        consecutives.append(args[n])

    if consecutives:
        if len(consecutives) == 1:
            sol.append(str(consecutives[0]))
            consecutives.clear()

        elif len(consecutives) == 2:
            sol.append(str(consecutives[0]))
            sol.append(str(consecutives[1]))
            consecutives.clear()

        else: # Must be a valid range (3 or more consecutive values)
            range_str = f'{consecutives[0]}-{consecutives[-1]}'
            sol.append(range_str)
            consecutives.clear()

    return ','.join(sol)