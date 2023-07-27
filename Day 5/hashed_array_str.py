def hashed_arr_str(string):
    hashed_string = 26 * [0]

    for char in string:
        hashed_string[ord(char) - ord('a')] += 1

    return hashed_string

print(hashed_arr_str('hashed'))