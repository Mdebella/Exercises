'''
Histogram

Description: Counts the frequency of values in a string

'''

#counts frequency value of a character in a string
def histogram(s):

    #initialize dictionary
    d = dict()

    #for character in string
    for c in s:

        #if character is not in the dictionary
        if c not in d:
            
            #sets key to a value of 1 for a single occurence of c
            d[c] = 1

        #else
        else:

            #sets key to increment +1 for every character that has already occured in the dictionary
            d[c] += 1

    #Exits the for loop once iteration is complete are returns the updated dictionary     
    return(d)

#sorts letter by highest frequency to lowest
def organize(s):

    #calls histogram variable
    d = histogram(s)

    #assigns dictionary items 
    t = d.items()

    #empty list
    L = []

    #splits pair into key and value
    for value,key in t:
        
        #appends key and value to list
        L.append((key,value))

    #sorts value in reverse
    L.sort(reverse = True)

    #creates empty list
    res = []

    # for every key, value in list
    for key,value in L:

        #add just value to list
        res.append(value)

    #returns final list
    return res

#runs the program
def main():

    #user input
    s = input('Enter string here (must be a string ''): ')

    #returns organize function
    return(organize(s))

#prints main function
print(main())


