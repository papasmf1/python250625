# DemoLoop.py 

value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---for in루프---")
lst = [100, "apple", 3.14]
for item in lst:
    print(item, type(item))

d = {"apple":100, "kiwi":200}
for k,v in d.items():
    print(k,v)

print("---수열함수---")
print(list(range(1,11)))
print(list(range(2000,2026)))
print(list(range(1,32)))

print("---리스트컴프리헨션---")
lst = list(range(1,11))
print(lst)
print([i**2 for i in lst if i>5])
tp = ("apple","kiwi","banana")
print([len(i) for i in tp])

print("---필터링함수---")
lst = [10, 25, 30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

print("---필터링 함수 사용---")
def getBiggerThan20(i):
    return i>20

itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)
