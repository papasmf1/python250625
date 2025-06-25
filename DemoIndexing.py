# DemoIndexing.py

#변수를 초기화
x = 100
y = 3.14 
strA = "python"
strB = "파이썬은 강력해"

print(dir())
print(len(strA))
print(len(strB))

#슬라이싱(인덱싱)
print(strA[0])
print(strA[0:2])
print(strA[:3])
print(strA[-2:])

#다중라인(Multiple line)
strC = """여기에 
다중라인을
저장합니다."""

print(strC)

#리스트를 연습
colors = ["red", "blue", "white"]
colors.append("white")
colors.insert(1, "pink")
print(colors)
print(type(colors))
#삭제
colors.remove("red")
print(colors)
print(colors[0])

#세트
print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print(type(a))
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


#튜플 
print("---tuple---")
tp = (10, 20, 30)
print(len(tp))
print(tp[0])

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#함수를 호출
result = calc(3,4)
print(result)

print("id:%s, name:%s" % ("kim", "김유신"))

