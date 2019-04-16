# Created by: Chris Asante
# Created on: 15-April-2019
# Created for: ICS3U
# 5-06
# The program accepts the letter and returns it as a hexidecimal value

def hexadecimal_converter(user_input):
    
    unicode_hex_value = {'A':'41', 'B':'42', 'C':'43', 'D':'44', 'E':'45', 'F':'46', 'G':'47', 'H':'48', 'I':'49', 'J':'4A', 'K':'4B', 'L':'4C', 'M':'4D', 'N':'4E', 'O':'4F', 'P':'50', 'Q':'51', 'R':'52', 'S':'53', 'T':'54', 'U':'55', 'V':'56', 'W':'57', 'X':'58', 'Y':'59', 'Z':'5A', 'a':'61', 'b':'62', 'c':'63', 'd':'64', 'e':'65', 'f':'66', 'g':'67', 'h':'68', 'i':'69', 'j':'6A', 'k':'6B', 'l':'6C', 'm':'6D', 'n':'6E', 'o':'6F', 'p':'70', 'q':'71', 'r':'72', 's':'73', 't':'74', 'u':'75', 'v':'76', 'w':'77', 'x':'78', 'y':'79', 'z':'7A'}
    
    return unicode_hex_value[user_input]

user_string = input('Enter a capital or lowercase letter: ')
print("\t")

for letter in user_string:
    converted_hex_value = hexadecimal_converter(letter)
    
    print("The hexadecimal value for the letter " + str(letter) + " is: " + str(converted_hex_value) + ".")
print("\t")