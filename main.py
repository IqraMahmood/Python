


#************

print("\t String Data Type")
ser = "My name is iqra mahmood"
print(ser)
print(type(ser))

print('\t int datatype')
int_type = 2233
print(int_type)
print(type(int_type))

print('\t Float datatype')
float_type = 2.9
print(float_type)
print(type(float_type))

print("\tComplex Data Type")
x = complex(1j)
print(x)
print(type(x))


#Fibonacci sequence
n1, n2 = 0,1
print("Fibonacci sequence:")
print(n1,"\n",n2)

for i in range(0,7):
    nth = n1 + n2
    print(nth)
    # update values
    n1 = n2
    n2 = nth


# # Task 2: Write python code that implements and prints iterative Fibonacci series.ntered by user are balanced or not.
def isbalanced(s):
    c = 0
    ans = False
    for i in s:
        if i == "(":
            c += 1
        elif i == ")":
            c -= 1
        if c > 0:
            return ans

    if c==0:
        return not ans
par = input("Enter par ")
print("Given string is balanced :", isbalanced(par))

