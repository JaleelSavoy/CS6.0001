'''
#################################
#Name: Jaleel Savoy
#Collaborators: NA
#Time: 8min
#Program: Finger Exercise --> max odd number calculator
    examines ten variables to find largest odd number
#################################
'''
def findMaxOddNumb():
    maxOdd = 0
    maxEven = 0
    for i in range(10):
        number = float(input("Enter a value: "))
        if (number % 2 != 0 and number > maxOdd):
            maxOdd = number
        elif (number % 2 == 0 and number > maxEven):
            maxEven = number
        else:
            print("Error")
    print("The max odd number: ", maxOdd)
    print("The max even number: ", maxEven)
        
findMaxOddNumb()