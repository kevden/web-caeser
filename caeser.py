def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - 65
    else:
        return ord(letter) -  97

def rotate_character(char, rot):
    if char.isalpha():
        if char.isupper():
            return chr((alphabet_position(char) + int(rot))%26 + 65)
        else:
            return chr((alphabet_position(char) + int(rot))%26+ 97)
    else:
        return char
	
def encrypt(text, rot):
    new_message= ''
    for character in text:
        new_character = rotate_character(character, rot)
        new_message += new_character
    return new_message
	
