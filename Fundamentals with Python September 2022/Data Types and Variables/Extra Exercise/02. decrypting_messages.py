key = int(input())
number_of_lines = int(input())
message = []

for _ in range(number_of_lines):
    char = ord(input())
    current_letter = chr(key + char)
    message.append(current_letter)

decrypted_message = ''.join(message)

print(decrypted_message)
