morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', " ": "\t"
         }

reverse_morse = {'.-': 'A',
                 '-...': 'B',
                 '-.-.': 'C',
                 '-..': 'D',
                 '.': 'E', '..-.': 'F', '--.': 'G',
                 '....': 'H', '..': 'I', '.---': 'J', 
                 '-.-': 'K', '.-..': 'L',
                 '--': 'M', '-.': 'N', '---': 'O', 
                 '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
                 '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', 
                 '-..-': 'X', '-.--': 'Y', '--..': 'Z', '\t': ' '}


def encode_to_morse(text):
         def encode_to_morse(text):
    text = text.upper()
    k = []
    for i in range(len(text)):
        k.append(morse[text[i]])
    text = ''.join(k)
    return k
    return text


def decode_from_morse(code):
    return code


def main():
    pass


if __name__ == '__main__':
    main()
