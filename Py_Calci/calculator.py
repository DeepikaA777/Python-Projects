# calculator.py
import math

def add(x, y):                                                      #Addition
    return x + y

def subtract(x, y):                                                 #Subtraction
    return x - y

def multiply(x, y):                                                 #Multiplication
    return x * y

def divide(x, y):                                                   #Division
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulus(x,y):                                                   #Modulus
    if y == 0:
        return "Cannot do Modules with Zero"
    return x % y

def power(x,y):                                                     #Power
    return x ** y

def squarert(x):                                                    #Square Root
    if x < 0:
        return "Cannot find a Square root for negative numbers"
    return int(math.sqrt(x)) #return a interger value      

def fact(x):                                                         #Factorial
    if x < 0:
        return "Cannot find a Factorial for negative numbers"
    return int(math.factorial(x))

def logarithm(x):                                                     #Logarithm
    if x <= 0:
        return "Invalid Number"
    return int(math.log(x))

def even_or_odd(x):                                                   #Even or Odd Number
    if x % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def is_prime(x):                                                       #Checking Prime Number or not                                    
    if x <= 1:
        return "Not a Prime Number"
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return "Not a Prime Number"
    return "Prime Number"

def rev_num(x):                                                         #Reversed number
    return int(str(x)[::-1])

def Count_Digits(x):        #Counting the digits 
    return len(str(abs(x))) #abs() is used for counting the negative numbers

def simple_interest(p,r,t):                                              #Simple Interest
    return p*r*t/100

def compound_interest(p,r,t):                                             #Compound Interest
    return p*((1+r/100)**t)-p

# <<-- Keep your exact interactive CLI unchanged, but make it only run when the file is executed directly. -->
if __name__ == "__main__":
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Factorial") #Factorial eg: 5!= 5*4*3*2*1=120
        print("9. Logarithm")
        print("10. Checks whether odd or even")
        print("11. Check whether a prime number")
        print("12. Reversing the Number")
        print("13. Counting the Numbers")
        print("14. Simple Interest Calculations")
        print("15. Compound Interest Calculations")
        print("16. Exit")
        print("...................................................................................................................")

        choice = input("Enter choice (1-16): ")

        if choice=='16':
            print("Exciting the calculator. GoodBye!")
            print("...................................................................................................................")
            break        #Exits the loop


        #Double Number Operation 
        if choice in ['1','2','3','4','5','6']:
           num1 = float(input("Enter first number: "))  
           num2 = float(input("Enter second number: "))

           if choice == '1':
               print("Result of the addition :", add(num1, num2))
               print("..................................................................................................................................................")

           elif choice == '2':
               print("Result of the subtraction :", subtract(num1, num2))
               print("..................................................................................................................................................")

           elif choice == '3':
               print("Result of the multiplication :", multiply(num1, num2))
               print("..................................................................................................................................................")

           elif choice == '4':
               print("Result of the division :", divide(num1, num2))
               print("..................................................................................................................................................")

           elif choice == '5':
               print("Result of the modulus :", modulus(num1, num2))
               print("..................................................................................................................................................")

           elif choice == '6':
               print("Result of the power:", power(num1, num2))    #Num1 is a operand and Num2 is a power that is, x^y
               print("..................................................................................................................................................")



        #Single number Operations
        elif choice in ['7','8','9','10','11','12','13']:
            num= int(input("Enter the Number: ")) #Square Root and Factorial have a single operand so we've initialized the num variable
            if choice == '7':
                print("Result of the square root :", squarert(num))
                print("...................................................................................................................")

            elif choice == '8':
                print("Result of the factorial :", fact(num))
                print("...................................................................................................................")

            elif choice == '9':
                print("Result of the logarithm :", logarithm(num))
                print("...................................................................................................................")

            elif choice == '10':
                print("Result of checking the even or odd :", even_or_odd(num))
                print("...................................................................................................................")

            elif choice == '11':
                print("Result of checking the prime number or not :", is_prime(num))
                print("...................................................................................................................")

            elif choice == '12':
                print("Result of reversed number :", rev_num(num))
                print("...................................................................................................................")

            elif choice == '13':
                print("Result of reversed number :", Count_Digits(num))
                print("...................................................................................................................")


        #Interest Calculations
        elif choice in ['14','15']:
            p= int(input("Enter the Amount "))
            r= int(input("Enter the rate "))
            t= int(input("Enter the time "))


            if choice== '14':
                print("Result of the simple interest :", simple_interest(p,r,t))
                print("...................................................................................................................")

            elif choice== '15':
                print("Result of the compound interest :", compound_interest(p,r,t))
                print("...................................................................................................................")

        else:
            print("Invalid Choice")
            print("...................................................................................................................")    
