message = input("Enter message: ")
shift = int(input("Enter shift amount: "))

result = ""

for ch in message:

    if ch.isupper():
        position = ord(ch) - ord('A')
        newPosition = (position + shift) % 26
        newCharacter = chr(newPosition + ord('A'))
        result += newCharacter

    elif ch.islower():
        position = ord(ch) - ord('a')
        newPosition = (position + shift) % 26
        newCharacter = chr(newPosition + ord('a'))
        result += newCharacter

    else:
        result += ch

print("Encoded message:", result)
