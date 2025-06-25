# Person.py 
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 인스턴스 생성 및 출력 예시
if __name__ == "__main__":
    p = Person(1, "홍길동")
    m = Manager(2, "김철수", "팀장")
    e = Employee(3, "이영희", "Python")

    p.printInfo()
    m.printInfo()
    e.printInfo()
