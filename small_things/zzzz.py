import pygame as pg
class hero:
    def __init__(self):
        self.name = 'Saurab'
        self.age =  10
        self.weight = 70
        print('My name is '+ self.name)
        self.printi()
    def printi(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Weight: " + str(self.weight))
        self.awesome()
    def awesome(self):
        my_name = input("Enter YOur Name: ")
        
        print('My name is ' + my_name +'\n'+ 'YOur name is ' + self.name)


