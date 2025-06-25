# DemoStr.py 

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(strA.capitalize())  # Python is very powerful
print(len(strA))  # 23
print(len(strB))  # 8
print("MBC2580".isalnum())  # True
print("2580".isdecimal())  # True

data = "<<<  spam and ham  >>>"
result = data.strip("<> ")  # Remove leading and trailing whitespace
print(data)  # <<<  spam and ham  >>>
print(result)  # spam and ham
result2 = result.replace("spam", "spam egg")  # Replace 'spam' with 'eggs'      
print(result2)  # spam egg and ham
lst = result2.split()  # Split the string into a list
print(lst)  # ['spam', 'egg', 'and', 'ham']
print(" ".join(lst))  # Join the list into a string with spaces

#정규표현식을 사용
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())  # 35th

#선택한 블럭 주석: ctrl + /
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())  # 35th

result = re.search("\d{4}", "올해는 2025년입니다.")
print(result.group())  # 2025

result = re.search("\d{5}", "우리동네는 51200입니다.")
print(result.group())  

result = re.search("apple", "This is apple.")
print(result.group())  
