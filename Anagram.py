'''

Anagram

6/9/22

Description: Reads input word and finds all possible anagrams of that word in dictionary.txt file

'''

#Input word
In = input('Enter word here: ')

def read(In):

    #Assigns word dictionary text file path to variable
    f = r'C:\Users\Frys Electronics\Desktop\Code Practice\words.txt'

    #Creates a tuple of the input word
    word = tuple(str(In))

    #Initializes empty list
    L = []

    #Opens text file as read only
    with open(f,'r') as word_dictionary:

        #iterates through every line in the dictionary file
        for line in word_dictionary:

            #creates tuple for every word in the dictionary file
            t = tuple(line.strip('\n'))

            #sorts the input word and the dictionary word and compares the two
            if sorted(t) == sorted(word):

                #If the words were the same then they are appended to the empty list
                L.append(line.strip('\n'))

        return(L)
                        
print(read(In))


    
