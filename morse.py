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
    text = text.upper()
    k = []
    for i in range(len(text)):
        k.append(morse[text[i]])
    text = ' '.join(k)
    return text


def decode_from_morse(code):
    return code


def main():
    while True:
        print("Вы хотите закодировать (1) или раскодировать(2) текст? 0 - выйти.")
        user_operation = input()
        if user_operation == "1":
            print("Введите текст:")
            text = input().upper()
            print(encode_to_morse(text))
        elif user_operation == "2":
            print("Введите код:")
            code = input()
            print(decode_from_morse(code))
        elif user_operation == "0":
            print("Всего доброго.")
            break


if __name__ == '__main__':
    main()
