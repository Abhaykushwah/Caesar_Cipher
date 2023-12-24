try:
    def shift_character(char, shift_amount):
        if char.isalpha():
            # Determine the case (upper or lower) of the character
            is_upper = char.isupper()
            
            # Shift the character within the range of its case
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift_amount) % 26 + ord('A' if is_upper else 'a'))
            return shifted_char
        else:
            # not char, return it unchanged
            return char

    def caesar_cipher(input_string, shift_amount):
        shifted_string = ''.join(shift_character(char, shift_amount) for char in input_string)
        return shifted_string

    def main():
        input_string = input("Enter a string: ")
        # Ensure the input is not empty
        if not input_string:
            print("Input string is empty. Exiting.")
            return
        
        # shift amount input by user
        shift_amount = int(input("Enter the shift amount (1-26): "))
        
        # shift amount is within the valid range
        if 1 <= shift_amount <= 26:
            ## Encrypt the input string using the Caesar cipher
            encrypted_string = caesar_cipher(input_string, shift_amount)
            
            print(f"Encrypted string: {encrypted_string}")
        else:
            print("Invalid shift amount. Exiting.")

    if __name__ == "__main__":
        main()

except FileNotFoundError:
	print("[-]File not Found.")
	
except KeyboardInterrupt:
	print("[-]Keyboard Interrupt.")