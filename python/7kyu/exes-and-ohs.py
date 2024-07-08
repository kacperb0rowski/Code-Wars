# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

#My solution

def xo(s):
    new_string = s.lower()
    x = new_string.count("x")
    o = new_string.count("o")
    if x == o or x == 0 and o == 0:
        return True
    else:
        return False