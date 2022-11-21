
class MorseConverter:

    def __init__(self):
        self.MORSE_CODE_DICT = {
                   'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----',
                   ', ': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   '/': '-..-.',
                   '-': '-....-',
                   '(': '-.--.',
                   ')': '-.--.-'
                   }

    def encrypt(self, message):
        """
        Convert English text into Morse Code
        """
        # Empty string to store the message to be ciphered
        cipher = ""
        for letter in message:
            if letter != ' ':
                # Checks the code for the corresponding letter
                # Adds the code to the empty string
                # Adds space to separate each coded letter
                cipher += self.MORSE_CODE_DICT[letter] + ' '

            else:
                # Adds space if there is space
                cipher += ' '

        return cipher

    def decrypt(self, message):
        """
        Convert Morse Code into English text
        """
        # Empty string to store the letter code that is decrypted
        decipher = ''
        # Empty string to store the letter code
        citext = ''

        for letter in message:
            # tracks the number of spaces
            i = 0
            if letter != ' ':
                # reset the value of spaces
                i = 0
                # stores the code into the empty string
                citext += letter
            else:
                # value of 1 indicates new character
                i += 1
                # value of 2 indicates new word
                if i == 2:
                    # adds space to separate the word
                    decipher += ' '
                else:
                    # decode the citext string into english letters
                    # convert all the keys from the dict into a list
                    key_list = list(self.MORSE_CODE_DICT.keys())
                    # convert all the value from the dict into a list
                    list_index = list(self.MORSE_CODE_DICT.values()).index(citext)
                    decipher += key_list[list_index]
                    # reset the citext into an empty string
                    citext = ''

        return decipher
