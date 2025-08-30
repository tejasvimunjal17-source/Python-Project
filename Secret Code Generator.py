#Python Programming Mini Project: "Secret Code Generator"

# This program can encode and decode messages using Caesar Cipher logic.

def encode(msg, shift):
    result = ""
    for ch in msg:
        if ch.isalpha():   # only shift letters
            if ch.isupper():
                # shift within A-Z
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
            else:
                # shift within a-z
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch   # keep spaces and symbols as they are
    return result

def decode(msg, shift):
    # decoding is just encoding with negative shift
    return encode(msg, -shift)

def main():
    while True:
        print("=== Secret Code Generator ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter the message to encode: ")
            try:
                s = int(input("Enter shift number: "))
                coded = encode(text, s)
                print("Encoded message:", coded, "\n")
            except:
                print("Invalid shift number!\n")

        elif choice == "2":
            text = input("Enter the message to decode: ")
            try:
                s = int(input("Enter shift number: "))
                decoded = decode(text, s)
                print("Decoded message:", decoded, "\n")
            except:
                print("Invalid shift number!\n")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()

    #Submitted By - Tejasvi Munjal
    #Mobile No. - +91 7982602495
    #Email Address - tejasvimunjal17@gmail.com
                                                #Submitted To - Vault of Code
