def pig_latin (word):
    first_letter = word[0].lower()
    if first_letter != "a" and first_letter != "e" and first_letter != "i" and first_letter != "o" and first_letter != "u":
        new_word = word[1:] + first_letter + "ay"
        return new_word
    else:
        new_word = word + "way"
        return new_word