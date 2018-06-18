#Question_1

year=int(input("enter year"))
if year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


#Question_2


length= int(input("Enter length:"))
breadth= int(input("Enter breadth:"))
if length==breadth:
    print("dimensions are square")
else:
    print("dimensions are rectangle")



#Question_3

a=int(input("Enter age of  person a:"))
b=int(input("Enter age of person b:"))
c=int(input("Enter age of person c:"))
if (a>b and a>c):
    print ("a is older")
elif (c>b and c>a):
    print("c is older")
elif(b>a and b>c):
    print("b is older")
if(a<b and a<c):
    print("a is younger")
elif(b<a and b<c):
    print("b is younger")
elif(c<a and c<b):
    print("c is younger")


#Question_4


points=int(input("enter the points upto 200:"))
if (points >1 and points <=50):
    print("No prize")
elif(points >51 and points<=150):
    print("wooden dog")
elif(points>151 and points<=180):
    print(" you won book")
elif (points>181 and points<=200):
    print(" you won chocolate")


#Question 5

a=int(input("enter the amount:"))
print(a)
if (a<=1000):
    print("Sorry, no discount")
elif (a*100 > 1000):
  print ("Cost is",((a*100)-(.1*a*100)))
else:
  print ("Cost is",a*100)












