# DemoOSRandom.py
import random

print(random.random())  # Generates a random float between 0.0 and 1.0
print(random.random())  # Generates a random float between 0.0 and 1.0
print(random.uniform(2, 5))
print(random.uniform(2, 5))

print([random.randrange(20) for i in range(10)])  # Generates a list of 10 random integers from 0 to 19
print([random.randrange(20) for i in range(10)])  # Generates a list of 10 random integers from 0 to 19

print("---샘플링---")
print(random.sample(range(20), 10))  # Generates a list of 10 unique random integers from 0 to 99
print(random.sample(range(20), 10))  # Generates a list of 10 unique random integers from 0 to 99

#로또번호
lst = list(range(1, 46))  # List of numbers from 1 to 45
print(random.shuffle(lst))  # Shuffles the list in place
print(lst[:5])

#파일명 다루기 
from os.path import * 

#raw string notation: r 
fileName = r"c:\python310\python.exe"

if exists(fileName):
    print("파일이 존재합니다.")
    print("파일의 크기:", getsize(fileName))
else:
    print("파일이 존재하지 않습니다.")

print("절대경로:", abspath("python.exe"))  # Prints the absolute path of the file
print("파일명만:", basename(fileName))  # Prints the base name of the file

#운영체제정보
import os
print("운영체제:", os.name)  # Prints the name of the operating system
print("환경변수:", os.environ)  # Prints the environment variables
#os.system("notepad.exe")

#특정 폴더의 파일 리스트
import glob 

result = glob.glob(r"c:\work\*.py")  
for item in result:
    print(item)  # Prints each Python file in the specified directory
