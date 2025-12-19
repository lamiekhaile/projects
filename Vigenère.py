
def vigenere(message, code):
    
    note = list(message.upper())
    hidden = list(code.upper())

    while len(hidden) < len(note):
        hidden.append(hidden[len(hidden) % len(code)])

    final = []
    for i in range(len(note)):
        v = (ord(note[i])-ord('A') + ord(hidden[i])-ord('A')) % 26
        num = chr(v + ord('A'))
        final.append(num) 

    return ''.join(final)





