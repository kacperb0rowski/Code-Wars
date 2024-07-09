# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string


#My solution

def fake_bin(x):
    new_lst = []
    for digit in x:
        if int(digit) >= 5:
            new_lst.append('1')
        else:
            new_lst.append('0')
    return ''.join(new_lst)