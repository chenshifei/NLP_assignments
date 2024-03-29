import re, sys


regex = re.compile(r'''
    (
        (?<=\.|\"|`|\?|\!)\s+(?=[A-Z]|\"|`|$)|
        \d+\.\d+|
        n\'t|
        \'[sd]|
        (\w+-)+\w+|
        ([A-Z]\w{0,3}\.)+|
        [,;:.!?\"%$&]|
        --|
        ``|
        \'\'?|
        \w+(?=n\'t)|
        \w+
    )
''', re.VERBOSE)

for line in sys.stdin:
    line = line + ' '
    for token in re.findall(regex, line):
        if token[0].isspace():
            print('')
        else:
            print(token[0])
