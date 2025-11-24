def check_vowel(character):
     for char in character:
        if char in 'aeiou':
            print(f"{character} is vowel")
        else:
            print(f"{character} is not vowel")
check_vowel("a")
check_vowel("z")