#################################
#Name: Jaleel Savoy
#Collaborators: Hugh Bothwell (stackoverflow)
#Time: 13min
#Program: isIN function
##accepts two strings as args and returns True if either sting
    ##occurs in the other, and false otherwise
#################################

def isIN(char, str):
    if (len(str) == 0):
        return False
    elif (len(str)==1):
        return char == str
    else:
        if char in str:
            return  True
        else:
            return False
                
# isIN("dog","log dog")
    #returns True
