#letter frequency in English
enLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
engFreqList = sorted(enLetterFreq.items(), key=lambda x: x[1], reverse=True)
#latin alphabets for referrence
latinAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
enFreqAlphabet = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

#recieve encoded message through console
ecnryptedMsg = input('Enter Encrypted Text')

#count letters in ecnryptedMsg
def getLetterCount(message):
    letterCount = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0, }

    for letter in message.upper():                     #this means letter is a string who's value is the n th letter of ecnryptedMsg
        if letter in latinAlphabet:
            letterCount[letter] += 1
             
    return(letterCount)
print('letterCount= ', getLetterCount(ecnryptedMsg))

#determine frequncy in message compare to frequency in language
def getFrequencyOrder(message):
    letterCount = getLetterCount(message)

    #"turn around" letters and count
    letterByFreq = {}
    for letter in latinAlphabet:
        if letterCount[letter] not in letterByFreq:
            letterByFreq[letterCount[letter]] = [letter]           #this creates a key in countLetter named after the amount of times
        else:
            letterByFreq[letterCount[letter]].append(letter)
    

    #Sorts letters by frequency and then puts them into a string (similart to engFreqList)
    for freq in letterByFreq:
        letterByFreq[freq].sort(key = enFreqAlphabet.find, reverse = False)
        letterByFreq[freq] =''.join(letterByFreq[freq])
    return(letterByFreq)

print(getFrequencyOrder(ecnryptedMsg))

#what to do about ambiguous characters?

#decode:
#create a new string
#check position of current character of the encoded text inside the string containing the latin alphabet by frequency within encoded text
#add the character at the same position inside the string sorted by frequency to the end of the new string