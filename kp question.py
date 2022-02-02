'''
while True:

    shape = input("Please enter the shape if you want to know area or would you like to exit? ").upper()

    if shape == "EXIT":
        print("Thank you!")
        break

    elif shape == "CIRCLE":
        radius = float(input("Please provide radius:"))
        area = 3.14 * radius * radius
        print( area)

    elif shape == "RECTANGLE":
        length = float(input("please provide length:"))
        width = float(input("please provide width:"))
        area = length * width
        print (area)

    elif shape == "SQUARE":
        side = float(input("please provied side:"))
        area = side * side
        print(area)

    elif shape == "TRIANGLE":
        side = float(input("please provied side: "))
        altitude = float(input("please provied altitude: "))
        area =1/2 * side * altitude
        print(area)

    else:
        print("Invalid entry")


s = "palindrome"
print(s[:3])
print(len(s))

while True:
    s = input("please enter the palondrome, Enter Exit if you do not want to play:  ").upper()
    if s == "EXIT":
        print("thank you")
        break

    reverse = s[::-1]
    if s == reverse:
       print("yes it is palondrome")
    else:
         print("no, it is not palondrome")


userinput = ""
while userinput != "EXIT":
    userinput = input("Please enter a word")
    print(userinput)
'''
a = input("enter a word not more than 15 chracters")
print(len(a))
if a<=15:
    print(a)
else:
    print("other")





