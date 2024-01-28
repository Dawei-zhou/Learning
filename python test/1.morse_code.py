"""
Morse Code Translator Function

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space.
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters.
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
- Non-alphabetic characters (like numbers or symbols) should not be translated.
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""

# 接受string 返回摩尔斯码string
def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }  
     
    # 先把接受到的输入string text 定义成新string 
    original_string = text   
    #  upper()方法让字符串升序，返回一个字符串
    uppercased_string = original_string.upper() 
    # list()方法转换字符串为列表(会把每个字符串的元素存入列表变成新元素，如果想分割就用split生成list)
    list_text=list(uppercased_string) 

    # 定义一个空字符串，准备操作该字符串后返回
    final_morse="" 
    # 对列表进行循环配对后添加字典的值进入finial_morse
    for element in list_text:
        if element in morse_code_dict:
            final_morse+=morse_code_dict[element]+" " 
        elif element==" ":
           final_morse=final_morse+"/"+" "
        else: 
            final_morse+=(" ") 

    return final_morse
    
        

 

# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.." 
                                                            # .... . .-.. .-.. --- / .-- --- .-. .-.. -..     
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -." 
                                                    #    .--. -.-- - .... --- -. 
print( morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ." 
                                                            # -- --- .-. ... . / -.-. --- -.. .
