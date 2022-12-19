class Num1:
    def __init__(self, name) -> None:
        self.name = name
    
class Num2:
    def __init__(self, age) -> None:
        self.age = age

class Num3:
    def prim1(self):
        print("Hello")

class Num4:
    def prim2(self):
        print("Goodby")

class Num5(Num1, Num2, Num3, Num4):
    def __init__(self, name, age) -> None:
        Num1.__init__(self, name)
        Num2.__init__(self, age)

    def __str__(self) -> str:
        return f'Name: {self.name}, age: {self.age}'




# num = Num5('Bob', 11)
# print(num)
# num.prim1()
# num.prim2()

