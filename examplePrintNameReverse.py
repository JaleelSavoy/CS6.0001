#print name example
def printName(firstName, lastName, reverse = False):
    if reverse:
        return print(lastName + "," + firstName)
    else:
        return print(firstName, lastName)
        
# printName('Jaleel', 'Savoy', True)
    #prints: Savoy, Jaleel
