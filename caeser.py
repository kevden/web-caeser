def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - 65
    else:
        return ord(letter) -  97

def rotate_character(char, rot):
    if char.isalpha():
        if char.isupper():
            return chr(alphabet_position(char) + int(rot) + 65)
        else:
            return chr(alphabet_position(char) + int(rot) + 97)
	
print(rotate_character('A', 13))
