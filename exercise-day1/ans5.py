class io():
    def __init__(self):
        self.str1 = "yash"


    def input(self):
        self.str1 = input("\n Write an Input : ")


    def output(self):
        print(f"\n The output is : {self.str1.upper()}")

str1 = io()
str1.input()
str1.output()