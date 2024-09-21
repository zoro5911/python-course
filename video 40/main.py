import random
import string

def add_random_chars(word, num_chars=3):
    """Helper function to add random characters to the start and end of the word."""
    random_chars = ''.join(random.choices(string.ascii_letters, k=num_chars))
    return random_chars + word + random_chars

def encode_word(word):
    """Encodes a single word into the secret code language."""
    if len(word) >= 3:
        # Remove the first letter, append it at the end, then add random characters
        word = word[1:] + word[0]
        encoded_word = add_random_chars(word)
    else:
        # If the word has less than 3 characters, reverse it
        encoded_word = word[::-1]
    return encoded_word

def decode_word(word):
    """Decodes a single word from the secret code language."""
    if len(word) < 9:
        # If the word has less than 3 characters (encoded), reverse it back
        decoded_word = word[::-1]
    else:
        # Remove 3 random characters from the start and end
        word = word[3:-3]
        # Move the last letter to the front
        decoded_word = word[-1] + word[:-1]
    return decoded_word

def encode_message(message):
    """Encodes a message into the secret code language."""
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    """Decodes a message from the secret code language."""
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    choice = input("Do you want to code or decode? (Enter 'code' or 'decode'): ").strip().lower()

    if choice == 'code':
        message = input("Enter the message to encode: ").strip()
        encoded_message = encode_message(message)
        print(f"Encoded message: {encoded_message}")
    elif choice == 'decode':
        message = input("Enter the message to decode: ").strip()
        decoded_message = decode_message(message)
        print(f"Decoded message: {decoded_message}")
    else:
        print("Invalid choice. Please enter 'code' or 'decode'.")

if __name__ == "__main__":
    main()
