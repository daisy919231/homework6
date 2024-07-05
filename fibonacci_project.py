from pywebio.input import input, FLOAT
from pywebio.output import put_text

#FIRST VERSION
# class SampleFibonacci:
#     def __init__(self):
#         self.additive1=0
#         self.additive2=1
#         you_choose=input('Enter a positive integer: ', type=FLOAT)
#         self.ending_number=you_choose

#     def __iter__(self):
#         return self
    
    
#     def __next__(self):
#         fibonacci_iterator=self.additive1   #0, 1
#         if int(self.ending_number) >= fibonacci_iterator:  #3>0, 3>1
#             starting_point= self.additive1 + self.additive2  #2,4
#             self.additive1=self.additive2   #1, 2
#             self.additive2=starting_point  #2,4
#             return fibonacci_iterator  #0,1
#         else:
#             raise StopIteration
            


# for i in SampleFibonacci():
#     put_text(i)

#SECOND VERSION -> does not stop, infinitive
# class SampleFibonacci:
#     def __init__(self):
#         self.additive1=0
#         self.additive2=1

#     def __iter__(self):
#         return self
    
    
#     def __next__(self):
#         fibonacci_iterator=self.additive1   #0, 1
#         starting_point= self.additive1 + self.additive2  #2,4
#         self.additive1=self.additive2   #1, 2
#         self.additive2=starting_point  #2,4
#         return fibonacci_iterator  #0,1


# for i in SampleFibonacci():
#     print(i)