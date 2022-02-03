# Problem1. The code for this problem displays the users name, address, city, state, ZIP, telephone number, and major.

name = "Robert Salinas"
address = "4030 Nichols Dr"
city = "Corpus Christi"
state = "Texas"
ZIP = 78410
telephonenum = "361-737-3531"
major= "Computer Science"

print(name, address, city, state, ZIP, telephonenum, major)

# Problem2. This problem takes the number of square feet in a tract of land and converts it to acres, then displays the answer converted to acres for the user.

totalsqft = float(input("Enter the total Square feet for the tract of land"))
numacres = totalsqft/43560
print("There is" ,numacres, "acres in this tract of land")

# Problem3. This code for this problem calculates how far the user will have traveled at 70mph given the number of hours the user inputs.
Speed = 70
Time = int(input("Please enter a time in hours"))
Distance=Speed*Time
print("At", Time, "hours, you will travel", Distance,"miles")

# Problem4. This code determines what stage in life the user is based on the age the provide
Age= int(input("Enter your age"))
if Age >= 0 and Age <= 1:
    print("This person is an infant")
elif Age > 1 and Age < 13:
    print("This person is a child")
elif Age >= 13 and Age < 20:
    print("This person is a teenager")
elif Age >= 20 and Age <=100:
    print ("This person is an adult")
else:
    print ("You entered an invalid number")

#Problem5. This code counts the number of pennies, nickels, dimes, and quarters entered by the user and displays if they more, less, or exactly a dollar. 
print("Make exactly one dollar by inputting the amount of pennies, nickels, dimes, and quarters needed")
pennies=float(input("Enter the number of pennies"))
nickels=float(input("Enter the number of nickels"))
dimes=float(input("Enter the number of dimes"))
quarters=float(input("Enter the number of quarters"))

if (pennies*.01 +  nickels*.05 + dimes*.10 + quarters*.25 == 1.00):
    print("Congratulations, you have a dollar")
elif (pennies*.01 +  nickels*.05 + dimes*.10 + quarters*.25 < 1.00):
    print("You have less than one dollar")
elif (pennies*.01 +  nickels*.05 + dimes*.10 + quarters*.25 > 1.00):
    print("You have more than one dollar")

#Problem6. The following code takes a year inputted by the user and determines wether or not it is a leap year.
year = int(input("Enter a year"))
if year%100 == 0 or year%4 == 0:
    print("The year you entered is a leap year")
else:
    print("The year you entered is not a leap year")

#Problem7. The following code take the height and weight from the user and displays their BMI and wether their health is optimal.
height=int(input("Enter your height in inches"))
weight=int(input("Enter your weight in pounds"))
bmi=weight*703/(height*height) 

print("Your BMI is ", bmi)

if bmi>=18.5 and bmi<=25:
        print("Your weight is optimal")
elif bmi<18.5:
        print("You are underweight")
elif bmi>25:
        print("You are overweight")

#Problem8. This code calculated and displayed Joes total amount paid to his broker and his total profit after buying and selling the stock.
num_shares=2000
paid=40.00
sold=42.75

print("Joe paid ",num_shares*paid," for the stock")
paidcom=((num_shares*paid)*.03)
print("Joe paid the broker", paidcom)

print("Joe sold the stock for ",num_shares*sold)
paidcom2=((num_shares*sold)*.03)
print("Joe paid the broker", paidcom2)

TotalProf = num_shares*sold-paidcom2-(num_shares*paid)-paidcom

print("Joes total profit was ", TotalProf)





