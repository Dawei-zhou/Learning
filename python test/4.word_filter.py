"""
Word Filter and Counter Function

Objective:
Write a function named 'word_filter_counter' that filters and counts specific words in a given text.

Function Parameters:
1. text (string): The text from which words will be filtered and counted.
2. filter_words (list of strings): A list of words to be filtered out from the text.

Instructions:
- The function should filter out the words from the text that are present in the filter_words list. The comparison should be case-insensitive.
- The function should return a dictionary. In this dictionary, the keys are the filtered words, and the values are the counts of how often these words appeared in the text.
- The text may contain punctuation marks and spaces. Only whole words, separated by spaces or punctuation, should be considered.

Example Test Cases:
1. word_filter_counter("Hello world, hello!", ["hello"]) should return a dictionary with the count of occurrences of "hello".
2. word_filter_counter("The quick brown fox.", ["the"]) should return a dictionary with the count of occurrences of "the".
3. word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]) should return a dictionary with the counts of occurrences of "is", "this", and "just".
4. word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]) should return a dictionary with the counts of occurrences of "we", "the", and "or".
"""

# 接受一个string， 一个列表，统计列表元素的分别出现在string中的次数
def word_filter_counter(text, filter_words):   
    # 加入正则表达式库
    import re  
    # 把输入的text 转换成小写后；用正则表达式把string中的单词提取到列表中
    words = re.findall(r'\b\w+\b', text.lower())  
    #定义一个空字典存储结果     
    result={} 
    # 遍历列表一个列表与另一个列表进行匹配
    for element in filter_words: 
        if element in words:    
            # count(元素)计算列表中元素的出现次数
            num_of_words=words.count(element) 
            # 生成一个新字典
            new={element:num_of_words}   
            # 新字典加入原字典
            result=dict(result,**new)
        else:   
            # 如果没有匹配项，新字典加入久字典且计数为0
            empty={element:"0"} 
            result=dict(result,**empty) 
    return result
            
    
 
    
        

    # Your code goes here
    # Implement the logic to filter words and count their occurrences
     # Delete this after implementing some code inside this function


# Test cases 
print(word_filter_counter("Hello world, hello!", ["hello"]))  # Expected output: {'hello': 2} 
print(word_filter_counter("The quick brown fox.", ["the"]))  # Expected output: {'the': 1}
print(   word_filter_counter(    "Is this real life? Is this just fantasy?", ["is", "this", "just"] ))  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(word_filter_counter(         "Do we see the big picture or just small details?", ["we", "the", "or"]))  # Expected output: {'we': 1, 'the': 1, 'or': 1}
