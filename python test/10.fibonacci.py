"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value):  
     list_data=[0,1]  
     # 三种情况
     if max_value<0: 
          return "Empty list or error message" 
     elif max_value==0:  
          # 移除索引是1的元素
          list_data.pop(1) 
          return list_data 
     # 定义变量
     final_number=0 
     i=0 
     a=0  
     # 当前列表的最大数不大于给定的最大数 
     while final_number< max_value:  
     # 生成一个新的数加入列表中，新的数等于列表最后两位数之和
          final_number=list_data[a]+list_data[a+1] 
          a+=1 
          # 新的数大于的话给定值的话就返回当前的list，否则加入原来的list中
          if final_number>max_value:   
               return list_data
          else:
               list_data.append(final_number)  
     # 返回列表 list_data
     return list_data


         


# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
