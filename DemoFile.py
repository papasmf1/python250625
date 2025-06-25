# DemoFile.py 

#파일에 쓰기
f = open("DemoFile.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()   

#읽기 
f = open("DemoFile.txt", "rt", encoding="utf-8")
print(f.read())  # 전체 읽기
f.close()




