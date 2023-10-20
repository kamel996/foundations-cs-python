# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# userInput = int(input("Enter a number to calculate its factorial: "))

# print(f"factorial of the number {userInput} is {factorial(userInput)}")



# def findDivisors(n):
#     divisor = []
#     for i in range(1, n + 1):
#        if (n % i == 0):
#             divisor.append(i)

#     return divisor


# userInput = int(input("enter number"))

# print(f"the divisors are {findDivisors(userInput)}")





# def replaceString(string):
#     divisor = ""
#     for i in string:
#      divisor =  i +  divisor
#      print(i)
#     return divisor


# userInput = (input("enter string"))

# print(f"the divisors are {replaceString(userInput)}")





# def even(arr):
#     newArr = []
#     for i in arr:
        
#         if i % 2 == 0:
#          newArr.append(i)

#     return newArr
        
# userInput = input("Enter a list of numbers separated by spaces: ")
# userInput = userInput.split()  
# userInput = [int(x) for x in userInput] 

# print(f"the even numbers of {userInput} are {even(userInput)}")





# def strongPassword(password):
#    has_upperCase = False
#    has_specialChar = False
#    contains_num = False
#    has_lowerCase = False

#    if len(password) < 8:
#        return False

#    for i in password:
#        if i.isupper():
#           has_upperCase = True
#        elif i.islower():
#            has_lowerCase = True
#        elif i in "$#~!?":
#            has_specialChar = True
#        elif i.isdigit():
#             contains_num  = True

#    return contains_num  and has_lowerCase and has_specialChar and has_upperCase
           


# user_input = input("Enter your password")



# if strongPassword(user_input):
#     print("Password is strong.")
# else:
#     print("Password is not strong")



