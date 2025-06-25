# DemoDict.py 

print("---dict형식---")
colors = {"apple":"red", "banana":"yellow"}
print(type(colors))
#입력
colors["kiwi"] = "green"
#삭제 
del colors["apple"]
print(colors)
#검색
print(colors['kiwi'])

#반복문
for item in colors.items():
    print(item)


