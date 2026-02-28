class Person:
    def __init__(self, n):
        self.n = n
class Student(Person):
    def __init__(self, n, gpa):
        super().__init__(n)
        self.gpa = gpa
    def display(self):
        print(f"Student: {self.n}, GPA: {self.gpa}")
n, g = input().split()
s = Student(n, float(g))
s.display()