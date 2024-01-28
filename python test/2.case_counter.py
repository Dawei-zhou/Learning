"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""

# 找字符串中大小写元素的数量
def case_counter(text):  
    # sum后面返回值是True or false， True 的话 sum 会加 1 ，false 不加；sum返回的是int
    count_lower = sum(c.islower() for c in text)
    count_upper = sum(c.isupper() for c in text)
    # 如果打印的是字符串，不能直接加入int，需要每部分都是string类型，需要加转换
    print("Uppercase letters: " + str(count_upper)+" Lowercase letters: " + str(count_lower))
    



# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
