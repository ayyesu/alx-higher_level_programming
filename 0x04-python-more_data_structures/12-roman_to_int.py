#!/usr/bin/python3


def roman_to_int(roman_string):
    # Create a dictionary of Roman numerals
    roman_dict = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    # Initialize a total as 0
    total = 0
    # Iterate over each letter in the string
    for i in range(len(roman_string)):
        # Get the current letter and the one after it
        curr_letter = roman_string[i]
        next_letter = roman_string[i + 1] if i + 1 < len(roman_string) else None
        # Check if the current letter is larger than the next one
        if roman_dict[curr_letter] >= roman_dict[next_letter]:
            # If it is, add it to the total
            total += roman_dict[curr_letter]
        else:
            # Otherwise, subtract it from the total
            total -= roman_dict
