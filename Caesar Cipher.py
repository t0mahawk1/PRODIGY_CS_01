def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts a given text using the Caesar Cipher.

  Args:
    text: The text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: The mode of operation, either 'encrypt' or 'decrypt'.

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  # traverse text
  for char in text:
    # Encrypt this character
    if char.isupper():
      char_code = ord(char)
      char_code = (char_code - 65 + shift) % 26
      result += chr(char_code + 65)
    elif char.islower():
      char_code = ord(char)
      char_code = (char_code - 97 + shift) % 26
      result += chr(char_code + 97)
    else:
      result += char

  # Check the mode and return appropriate result
  if mode == 'decrypt':
    shift = -shift
    return caesar_cipher(result, shift, 'encrypt')
  else:
    return result

# Get input from user
text = input("Enter your message: ")
shift = int(input("Enter the shift value (1-25): "))
mode = input("Enter mode (encrypt/decrypt): ")

# Check if mode is valid
if mode not in ['encrypt', 'decrypt']:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Call the function and print the result
result = caesar_cipher(text, shift, mode)
print("The", mode, "ed text is:", result)
