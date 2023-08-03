# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

#Python Object-Oriented Programming
class Employee:
    #methods are functions inside class
    #methods can be class methods or instance methods
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def printall(self):
        return(self.first , self.last, self.pay)
    def func2():
        print('yoyoyo')
#Bee is instance, Employee is class.
a = Employee('ㅁ','ㅠ',3)
Employee.func2()
Employee.func2(a)
# <-- a 라는 인자가 자동으로 들어감