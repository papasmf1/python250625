# Python 클래스 작성
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)  # Person 클래스의 생성자를 호출
        self.title = title
    
    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 호출
        print(f"Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)  # Person 클래스의 생성자를 호출
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 호출
        print(f"Skill: {self.skill}")


# 테스트 코드 작성
person1 = Person(1, "Alice")
manager1 = Manager(2, "Bob", "Project Manager")
employee1 = Employee(3, "Charlie", "Python Developer")

# Person 객체는 title이나 skill 없이 생성
person2 = Person(4, "David")
manager2 = Manager(5, "Eva", "Team Lead")
employee2 = Employee(6, "Frank", "Java Developer")

person3 = Person(7, "Grace")
manager3 = Manager(8, "Hannah", "Operations Manager")
employee3 = Employee(9, "Ivy", "Data Scientist")

person4 = Person(10, "Jack",)
manager4 = Manager(11, "Kathy", "Product Manager")

# 테스트 출력
test_cases = [person1, manager1, employee1, person2, manager2, employee2, 
              person3, manager3, employee3, person4, manager4]

for person in test_cases:
    person.printInfo()  # 각 객체의 printInfo 메서드 호출
