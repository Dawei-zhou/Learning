"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

# 先分别存到两个列表，每个列表两个元素，一个月份一个日  
# 然后建一个字典存年份代表数字几
# 然后列表的月份元素分别比较字典看是几月份，提取后比较，然后三种情况下再比较日  
#再判定日后返回判定
def date_passed(todays_date, scheduled_date):  
    import re
    today=todays_date.split(" ")
    scheduled=scheduled_date.split(" ")
    Month_info={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}  
    today_month=0 
    scheduled_month=0  
    # 判断月份是否相同
    for element in today : 
        if element in Month_info:  
            today_month=int(Month_info.get(element)) 
    for month in scheduled :
        if month in Month_info: 
            scheduled_month=int(Month_info.get(month))   
    if today_month>scheduled_month:  
        print("Scheduled date has passed") 
    elif today_month<scheduled_month: 
        print("Scheduled date is yet to pass") 
    # 月份相同的情况再比较具体日期是否相同
    elif today_month==scheduled_month:   
    # 正则表达式从string中提取出日期的具体数字进行比较
        a=re.findall("\d+", todays_date)
        b=re.findall("\d+", scheduled_date) 
    # 把提取到的数字string 转换成int string 才可以比较大小
        int_today= int(a[0])
        int_scheduled= int(b[0]) 
    # 年份相同情况下 具体日期的3种不同情况
        if int_today==int_scheduled:  
            print("Scheduled date is today")  
        elif int_today<int_scheduled: 
            print("Scheduled date is yet to pass")
        else:
            print("Scheduled date has passed")

    

            
            
        
         
    
    # Your code goes here
    # Implement the logic to compare the dates and print the appropriate message
     # Delete this after implementing some code inside this function


# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
