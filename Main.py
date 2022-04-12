#Gunnar Stewart

#This program explores the use of
#simple operators in a vareity of
#different contexts. The listed
#requirments for the integration
#project should be followed
#approximatly sequential with
#this program


#Input function
username=input("What is your name? ")
#Greets user with sep= and end= arguements
print("Welcome", username, end="!", sep=" ")

base_number=input("\n\nGive me your favorite integer value: ")
integerBaseNumber=int(base_number)
#Exponent operation
print("Here is your favorite integer cubed:", integerBaseNumber**3)
cubed=float(integerBaseNumber**3)
#Multiplication operation
print("Here is your number cubed and then multipled by 1/2:", cubed*0.5)

real_number=input("\nGive me any real number: ")
floatRealNumber=float(real_number)
#Division operation
print("If we divide your real number by 2, we get", floatRealNumber/2.0)

divisor=input("\nGive me a rational number between 0 and 1: ")
floatDivisor=float(divisor)
#Dividend and floor division
print("Your rational number goes into 4 atleast", 4//floatDivisor, 'times')
#The divisor is reqired to be
#a positive real number in
#order for remainder to work
#correctly because negative
#floats seem to cause strange
#outputs.
print("The remainder being approximatly", 4%floatDivisor)

num1=input("\nEnter first real nunber: ")
num2=input("Enter second real nunber: ")
floatnum1=float(num1)
floatnum2=float(num2)
#Addition operation
print("The sum of your first and second real numbers are", floatnum1+floatnum2)
#Subtraction operation
print("The difference of your first and second real numbers respectively are", floatnum1-floatnum2)

repetition=input("\nEnter a whole number for how many times you want to scream 'AMONG US!': ")
integerRepetition=int(float(repetition))
#Repetition of a string
print("AMONG US! "*integerRepetition)

print("\nWhat is the appropriate punctuation to end the following sentence:")
print("'Sarah, did you take out the trash like I asked'")
p1=input("Your answer: ")
#concatenation using '+' for strings
print("Sarah, did you take out the trash like I asked"+p1)

#We assume we are dealing with a rectangle in the xy-plane
#such that negative geometries are regarded equvilent to positive geometries.
side1=abs(float(input("Enter a numeric side length of a rectangle: ")))
side2=abs(float(input("Enter a another numeric side length of a rectangle: ")))
recArea=abs(side1*side2)
if side1==side2:
    print("You have a special case of rectangle, a square with area", recArea)
else:
    print("The area of your rectangle is", recArea)

#Guessing game using a loop properties of calling a
#defined function
def guessGame():
    guessNum = float(input("\nGuess the number I am thinking of between 1 and 10: "))
    if guessNum==9:
        print("That's correct!")
    elif guessNum%2==0:
        print("Hint: It is an odd number.")
        guessGame()
    elif guessNum<=5:
        print("Hint: The number is greater than 5.")
        guessGame()
    elif guessNum!=9:
        print("Close, try again.")
        guessGame()

guessGame()

import math

#The following code uses the theorem of Papus to
#find the volume of a torus.
def volTorus(crossArea, distance):
    volume=crossArea*distance
    print("The volume of your torus is: ", format(volume, '.2f'))

print("Lets find the volume of a torus of your choosing.")
shape=int(input("Pick a cross-sectional shape for your torus (1=Ellipse, 2=Rectangle): "))
if shape==1:
    xRad=abs(float(input("Enter value for x semi-axis of ellipse: ")))
    yrad=abs(float(input("Enter value for y semi-axis of ellipse: ")))
    innerRad=abs(float(input("Enter the inner radius of your torus: ")))
    dis=2*math.pi*(innerRad+xRad)
    area=math.pi*xRad*yrad
    volTorus(area,dis)
elif shape==2:
    side1=abs(float(input("Enter hieght of rectangle: ")))
    side2=abs(float(input("Enter width of rectangle: ")))
    innerRad=abs(float(input("Enter the inner radius of your torus: ")))
    dis=2*math.pi*(innerRad+(side2)/2)
    area=side1*side2
    volTorus(area,dis)

vero=0
elnum1=float(input("Give a real number:" ))
if (elnum1>0 and elnum1%1==0):
    print("Your number is a natural number.")
if not (-9<=elnum1<=9) or elnum1%1!=0:
    print("Your number is not a single digit integer.")
if elnum1%1==0 and elnum1<0:
    print("Your number is a negative integer.")

n=len(input("Type something: "))
for i in range(1,n+1):
    print("Wow, that was pointless.")

n2=int(input("Give me a positive integer greater than 1: "))
while n2>0:
    n2=n2-1
    print(n2+1)
