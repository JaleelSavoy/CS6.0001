'''
#################################
#Name: Jaleel Savoy
#Collaborators: NA
#Time: 4min
#Program: Finger Exercise --> convert string of numbers
    prints the sum of numbers in s
#################################
'''
s = "1.23, 2.4, 4.3, 3.123"
s = s.split(",")
sumS = 0

for i in s:
    i = float(i)
    sumS += i
print(sumS)

    