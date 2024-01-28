"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.
2. r (float): Annual interest rate in decimal.
3. n (integer): Number of times interest is compounded per year.
4. t (integer): Number of years for investment.

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""

# 需要计算浮点数amount，返回一个string
def compound_interest_calculator(P, r, n, t): 
    A= (P*(1+r/n)**(n*t)) 
# 浮点数需要转换成string 再加入到最后的string中进行返回
    Sentence=str(A)+" after "+str(t)+" years"
    return Sentence
   


# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years
