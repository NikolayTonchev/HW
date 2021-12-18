
input = str(input('Enter text:'))
if input == '':
    print('Empty input!')
    quit()

#apple and banana one apple one banana a red apple and a green apple

input_split = input.split()
dictionary = {}

def count(elements):
    # check if each word has '.' at its last. If so then ignore '.'
    if elements[-1] == '.':
        elements = elements[0:len(elements) - 1]
   
    # if there exists a key as "elements" then simply
    # increase its value.
    if elements in dictionary:
        dictionary[elements] += 1
   
    # if the dictionary does not have the key as "elements" 
    # then create a key "elements" and assign its value to 1.
    else:
        dictionary.update({elements: 1})
    
# take each word from lst and pass it to the method count.
for elements in input_split:
    count(elements)
   
# print the keys and its corresponding values.
for allKeys in dictionary:
    print ("Frequency of ", allKeys, end = " ")
    print (":", end = " ")
    print (dictionary[allKeys], end = " ")
    print() 