'''
Project 3 - NATO Alphabet - Fall 2025  
Author: Lamiek Haile  lamiekh

This program reads a NATO alphabet file and a list of identifiers, categorizes each as a TAG, VIN, or invalid, and prints their NATO spellings along with totals for valid and invalid identifiers

I have neither given or received unauthorized assistance on this assignment.
Signed:  Lamiek Haile.
'''   
    
def get_dictionary():
    '''
    Reads the NATO alphabet file and builds a dictionary that maps each
    character to its corresponding code word. Also adds entries for the
    space character and the dash character.
    Parameters: none
    Return: a dictionary containing character-to-code-word mappings
    '''     
    dictionary = {}
    with open('alphabet.txt') as file:
        for line in file:
            parts = line.split()
            
            letter = parts[0]
            word = parts[1]
            
            dictionary[letter] = word
            
        dictionary[' '] = "Space"
        dictionary['-'] = "Dash"
        
    return dictionary


def categorize_identifier(identify):
    '''
    Determines whether the given identifier is a TAG, a VIN, or INVALID
    based solely on its length.
    Parameters:
        identify - the identifier string to categorize
    Return: a string representing the category ('TAG', 'VIN', or 'INVALID')
    '''    
    num = len(identify)
    
    if num >=5 and num<=8:
        return 'TAG'
    elif num == 17:
        return 'VIN'
    else:
        return 'INVALID'
    
    
def get_spelling(alphabet_dict,identifier):
    '''
    Uses the alphabet dictionary to convert an identifier into its NATO
    phonetic spelling, with each code word separated by a single space.
    Parameters:
        alphabet_dict - the dictionary mapping characters to code words
        identifier - the identifier to spell out
    Return: a string containing the NATO spelling of the identifier
    '''
    nato = []
    
    for i in identifier:
        word = alphabet_dict[i]
        
        nato.append(word)
        
    result = ''
    
    
    for i in range(len(nato)):
        if i == 0:
            result += nato[i]
        else:
            result += ' ' + nato[i]
            
    return result



def main():
    '''
    Controls the overall program flow: loads the alphabet dictionary,
    processes each identifier from the input file, prints its category
    and spelling when valid, and displays counts of valid and invalid
    identifiers at the end.
    Parameters: none
    Return: none
    '''    
    var1 = get_dictionary()
    
    valid_counter = 0
    invalid_counter = 0
    with open('identifiers.txt') as file:
        for i in file:
            newvar = i.strip('\n')
            newvar = newvar.upper()
            var2 = categorize_identifier(newvar)
            print(var2 + ': ' + newvar)
            if var2 == 'TAG' or var2 == 'VIN':
                print(get_spelling(var1, newvar))
                valid_counter += 1
                
            elif var2 == 'INVALID':
                invalid_counter+= 1
            print()
                
                
        print('Number of valid identifiers:', valid_counter)
        print('Number of invalid identifiers:', invalid_counter)




if __name__ == '__main__':
    main()    
