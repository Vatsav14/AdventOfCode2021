with open("input.txt", "r") as file:
    data = [x.split() for x in file.readlines()]

def part1():
    count = 0
    for each in data:
        consider = each[-4:]
        for every in consider:
            if len(every) == 2 or len(every) == 3 or len(every) == 4 or len(every) == 7:
                count += 1
    return count
                

print(part1())

#   0   a b c   e f g       6
#   1       c     f     2
#   2   a   c d e   g      5
#   3   a   c d   f g      5
#   4     b c d   f       4
#   5   a b   d   f g      5
#   6   a b   d e f g       6
#   7   a   c     f      3
#   8   a b c d e f g        7
#   9   a b c d   f g       6

# Frequencies:
# a : 8
# b : 6 (Unique)
# c : 8
# d : 7
# e : 4 (Unique)
# f : 9 (Unique)
# g : 7

# Strategy (Pain):
# - Deal with the unique frequencies
# - Using this, we get the mapping for b, e, f, g
# - Now we find a using set difference of signals for 1 and 7 since we know what they are
# - Now whatever is left over with frequency 8 will be c
# - Now whichever letter doesn't have a mapping in the display for 4 will be d
# - And whatever is left will be g
