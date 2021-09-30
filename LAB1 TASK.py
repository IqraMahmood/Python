# Task 1: Write python code that calculates and prints the squares of all the items of the list.
my_list = [1,2,3,4,5]
for i in my_list:
    print(i*i)
# Task 2: Write python code that calculates and prints the factorial of a user defined number.
# user_no = int(input('Enter number to calcuate factorial'))
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print("The factorial of number is ", factorial(user_no))
#
# # Task 3: Write python code that calculates and prints the number of uppercase and lowercase letters in a user defined sentence.
# sen = input("Enter sentence to find upper and lower letters")
# ind = 0
# upper = 0
# lower =0
# for i in sen:
#     x = sen[ind].isupper()
#     if x == True:
#         upper = upper+1
#     else:
#         lower =lower+1
#     ind = ind+1
# print(upper,lower)
# #Task 4: Write python code that determines and prints either user defined number is palindrome or not.
# num = input("Enter number")
# def reverse(n):
#     num = str(n)
#     return (num[::-1])
# def palindromic(n):
#     rev = reverse(n)
#     if num == rev:
#         print ("Palindromic")
#     else:
#         print("Not Palindromic")
# palindromic(num)
#
#
# # Task 5: Write python code that finds and prints the list of words that are longer than a user defined number “n” from a given list of words.
# given_list = ['my','name','is','iqra','mahmood']
# number = int(input('enter no '))
# final_list = []
# for i in given_list:
#     if len(i)>number:
#         final_list.append(i)
# print(final_list)
#
# # # Task 6: Write python code to print a list, sorted in ascending order by first element and then by last element in each tuple from a given list of non-empty tuples.
# our_list = [(1,2),(5,7),(9,3)]
# our_list.sort(key = lambda x: x[0])
# print(our_list)
# our_list.sort(key = lambda x: x[-1])
# print(our_list)
