import os
from re import X

# 1 task
#os.mkdir("folder") - creating new directory
#os.rmdir("folder") - deleting the directory

# os.mkdir("hmm")
# os. chdir("hmm") - changing/updating the directory
#os. listdir("hmm") - read the directory

# 2 task
# a = 0
# n = int(input("Please enter the number of integers"))
# for l in range(n):
#   ele = int(input())
#   a = a + ele
# print (a)  

# 3 task
# def f1(func):
#     def s_f():
#         print("Start")
#         func()
#         print("finish")
#     return s_f    

# @f1
# def check(): 
#     n = '29'
#     print(type(n))
#     conv_n = int(n)
#     print(type(conv_n)) 
# check()

# 4 task

# class Main:
#     def __init__(self, l, w):
#          self.length=l
#          self.width=w

#     def Area(self):
#          s = (self.length * self.width)
#          print("S = ",s)         
        
#     def Perimeter(self):
#          p = (self.length + self.width)*2
#          print("P = ",p)

# class Subm(Main):
#      def __init__(self, l, w):
#          super().__init__(l, w)

# recTA = Subm(45,29).Area()
# recTP = Subm(45,29).Perimeter()