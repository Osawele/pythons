# I've come to realize that python3's round() function only rounds ties to even i.e it rounds to the .5 to the nearest even function
# e.g, 3.5 rounds up normally to 4, but a number like 2.5 weirdly rounds down to 2. This is no mistake on pythons part; like I said,
# python3.0 only ROUNDS TIES TO EVEN. Anyway, below is a user-defined function that rounds off numbers normally.

def round_off():
    