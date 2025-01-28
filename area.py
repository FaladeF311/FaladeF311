# for loop
#program to find the sum of all numbers stored in a list
#List of numbers
# numbers= [6,5,3,8,4,2,5,4,11]
# sum = 0
# for val in numbers:
#      sum= sum+val
#  print("The sum is", sum)
# range function
# range(Start, Stop, Step size)
# print(list(range(2,20,3)))
# genre= ['pop', 'rock', 'jazz']
# for i in range(len(genre)):
#    print("I like", genre)
# digits = [0,1,5]
# for i in digits:
#     print(i)
# else:
#     print("No items left.")
# count=int(input('How many times do you want to say "Hello" :'))
# i=1
# while i<= count:
#     print('Hello')
#     i+=1
# print('Job is done! Thank you!!')
# for val in "String":
#     if val== "i":
#         break
#     print(val)
# print("The end")
#write a python program to find the sum of numbers btw 1 and 20 using a for loop
# numbers= list(range(1,20,1))
# sum= 0
# for val in numbers:
#     sum+= val
# print("The sum is ", sum)

# numbers= list(range(1,1000,2))
# sum= 0
# for val in numbers:
#     sum+= val
# print("The sum is ", sum)
name= input("What is your name?\n")
if len(name) <= 3:
    print("Name must be more than 3 characters")
elif len(name) >= 50:
    print("Name cannot be more than 50 characters")
else:
    print("Name is accepted")