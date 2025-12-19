

d = {}

for i in range(26):
    d[chr(ord('A') + i)] = i
    
def decrypt(string):
    
    
    string1 = string.upper()
    
    
    final = []
    for i in string1:
        if 'D' <= i <= 'Z':
            final.append(chr(ord(i) - 3))
        elif 'A' <= i <= 'C':
            final.append(chr(ord(i) + 23))
        
    return ''.join(final)