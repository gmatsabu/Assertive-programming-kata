MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 


 
def lettersToMorseCode(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
  
            
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            
            cipher += ' '
  
    return cipher 
   
def morseCodeToLetters(message): 
  
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
  
       
        if (letter != ' '): 
   
            i = 0
  
            citext += letter 
   
        else:  
            i += 1
  
            if i == 2 : 
  
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = '' 
  
    return decipher 

def main(): 
    message = "Teboho-matsabu"
    result = lettersToMorseCode(message.upper()) 
    assert len(message) !=0 ,"Does not have the same lenth"
    print(len(message))
    print (result) 
  
    message = "- . -... --- .... --- -....- -- .- - ... .- -... ..-"
    message_length = list(message.split(' '))
    result  = morseCodeToLetters(message) 
    assert len(message) !=0,"Please cheack your input and try again"
    print (result) 
    print(len(message_length))
  
if __name__ == '__main__': 
    main() 

