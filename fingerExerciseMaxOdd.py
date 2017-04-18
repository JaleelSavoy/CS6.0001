'''
#################################
#Name: Jaleel Savoy
#Collaborators: NA
#Time: 8min
#Program: Finger Exercise --> max odd number calculator
    examines three variables to find largest odd number
#################################
'''

x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
z = float(input("Enter a number: "))
arrayXYZ = [x,y,z]
max = 0
counter = 0

for i in arrayXYZ:
    if i % 2 == 0:
        counter += 1
        if counter == len(arrayXYZ):
            print("no odds")
    elif i % 2 != 0:
        if i > max:
            max = i
print("Max odd number: ", max)