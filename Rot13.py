def rot13(message):
    lst = [i for i in message]
    for i in range(len(lst)):
        ascii = ord(lst[i])
        if ascii in range(97,123):
            if ascii+13 > 122 : 
                pos = 122 - ascii
                ascii = 96 + 13-pos
                lst[i] = chr(ascii)
            else : 
                lst[i] = chr(ascii+13)
        elif ascii in range(65,91):
            if ascii + 13 > 90  : 
                pos = 90 - ascii
                ascii = 64 + 13-pos
                lst[i] = chr(ascii)
            else:
                lst[i] = chr(ascii+13)
        else : 
            continue
    return ''.join(lst)
