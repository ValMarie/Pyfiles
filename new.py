#1 -- reversing the list
# x = [1, 2, 3, 4]

# def reverse(num):
#     mode = len(num) - 1
#     arr = []

#     while mode >= 0:
#        last = num[mode]
#        arr.append(last)
#        mode = mode - 1
#     return arr

# print (reverse(x))

#2 --To count number of element in a list without the len()
# y = [23, 5, "s", "people", 4.66, True]

# def count(con):
#     i = 0
  
#     for x in con:
#         i = i + 1
#     return i
    
# print (count(y))

#3 --input
# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print (name + " likes " + color)



#4 --coversion
# weight = input("What is your weight? ")
# weight_in_kg = int(weight) * 0.45
# print (weight + " pounds")
# print ("To Kilogrammes = " + str(weight_in_kg) + "kg")

# formatted str
# print (f'To Kilogrammes = {str(weight_in_kg)}kg')



#5 --Game Module: A Guessing Game
# secret_country = "ARGENTINA"
# guess_count = 0
# guess_limit = 2

# guess = input('Where was Pope Francis born? ')
# while guess_count < guess_limit:
#     guess = input ("Wrong, Guess again: ")
#     guess_count += 1

#     if guess == secret_country:
#         print ("Correct, You won!")
#         break
# else:
#     print ("Sorry, try again later!")


# 6 --Game Module: A Car Game #
# command = ""
# car_started = False
# while True:
#     command = input('>> ').lower()    
#     if command == "start":
#         if car_started:
#             print ("Car already started!")
#         else:
#             car_started = True
#             print ("Car started...Ready to go!")
#     elif command == "stop":
#         if not car_started:
#             print ("Car already stopped!")
#         else:
#             car_started = False
#             print ("Brakes applied...Car stopped.")
#     elif command == "help":
#         print (''' start - to start the car.\n stop - to stop the car.\n quit - to exit''')
#     elif command == "quit":
#         command = input("Are you sure you want to quit? Y/N? ").lower()
#         command == "y" or "n"        
#         if command == "y":
#             break
#     else:
#         print ("Sorry, I don't understand that command...")



# prices = [10, 20, 30, 40]
# total = 0
# for item in prices:
#     total += item
# print (total)



# 7---Designed letter "E and F"---#

# METHOD 1
# (F)
for x in range(2):
    print ("x" * 5)
    for y in range(1):
        print ("x" * 2)
print ("x" * 2)

print ("=" * 10)

# (E)     
# for x in range(2):
#     print ("x" * 5)
#     for y in range(1):
#         print ("x" * 2)
# print ("x" * 5)

# METHOD 2
# (F)
# numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     print ("x" * number)

# METHOD 3
#(F)
# numbers = [5, 2, 5, 2, 2]

# for  number in numbers:
#     result = ""
#     for num_count in range(number):
#         result += "x"
#     print (result)


# classes
# class Letter:
#     def __init__(self, x, y):           # constructor
#         self.x = x
#         self.y = y

#     def alpha(self):
#         print ('alpha')

#     def beta(self):
#         print("beta")


# alphabet = Letter("a", "b")
# alphabet.beta()
# alphabet.leta = "xyz"       # class attr
# print(alphabet.x)

#Dice roll
# import random

# class Dice:
#     def roll(self):
#        first = random.randint(1, 6)
#        second = random.randint(1, 6)
#        return first, second


# dice = Dice()
# print (dice.roll())
