encoding = "utf-8"

def decode(text):
	
    text_bytes = text.encode(encoding) # The text encoded as bytes
    output = [] # The output characters

    for char in text_bytes:
        if char == "<".encode(encoding)[0]:
            print("Found opening of a token")
        elif char == ">".encode(encoding)[0]:
            print("Found closing of a token")
        
        output.append(char) # Add the character to our output
    
    return bytes(output)

print(decode("supercalifragilisticexpialidocious <35,34>").decode(encoding))