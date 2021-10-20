# 부모 클래스 정의
class Person(object):
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    #기존 초기화 메서드를 덮어 쓰기(override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모의 생성자 호출
        Person.__init__(self, name, phoneNumber)
        self.name = name
        self.phoneNumber = phoneNumber

        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID



p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")


