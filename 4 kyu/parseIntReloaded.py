'''
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']


def parse_int(string):
    if '-' in string:
        string = string.replace('-', ' ')

    if ' and ' in string:
        string = string.replace(' and ', ' ')

    num_words = string.split()
    numbers = []
    for num in num_words:
        if num in ONES:
            numbers.append(ONES.index(num))
        elif num in TENS:
            numbers.append((TENS.index(num) + 2) * 10)
        elif num == 'hundred':
            numbers[-1] *= 100
        elif num == 'thousand':
            numbers = [n * 1000 for n in numbers]
        elif num == 'million':
            numbers = [n * 1000000 for n in numbers]

    return sum(numbers)
