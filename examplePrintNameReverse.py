#print name example
def printName(firstName, lastName, reverse):
    if reverse:
        return print(lastName + "," + firstName)
    else:
        return print(firstName, lastName)
        
printName('Jaleel', 'Savoy', True)