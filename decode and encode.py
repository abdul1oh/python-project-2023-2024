

def encode(soz,son):
    alphabit = 'abcdefghijklmnopqrstuvwxyz'
    shifr_soz = ''
    for harf in soz:
        if harf in alphabit:
            index = alphabit.index(harf)
            yangi_index = (index + son) % len(alphabit)
            shifr_soz += alphabit[yangi_index]
        else:
            shifr_soz += harf
    return shifr_soz
print(encode("abdulloh",4))

def decode(soz,son):
    alphabit = 'abcdefghijklmnopqrstuvwxyz'
    shifr_soz = ''
    for harf in soz:
        if harf in alphabit:
            index = alphabit.index(harf)
            yangi_index = (index - son) % len(alphabit)
            shifr_soz += alphabit[yangi_index]
        else:
            shifr_soz += harf
    return shifr_soz
print(decode("efhyppsl",4))




def encode(soz, son):
    soz = soz.replace(" ", "")
    if son == 1:
        return soz

    qatorlar = []
    for i in range(son):
        qatorlar.append("")

    qator = 0
    qadam = 1
    for harf in soz:
        qatorlar[qator] += harf
        if qator == 0:
            qadam = 1
        elif qator == son - 1:
            qadam = -1
        qator += qadam
    javob = ''.join(qatorlar)
    return javob

def decode(encoded_soz, son):
    if son == 1:
        return encoded_soz

    n = len(encoded_soz)
    qator_hisobi = [0] * son
    qator = 0
    qadam = 1
    for i in range(n):
        qator_hisobi[qator] += 1
        if qator == 0:
            qadam = 1
        elif qator == son - 1:
            qadam = -1
        qator += qadam

    qatorlar2 = []
    start = 0
    for i in range(son):
        qatorlar2.append(encoded_soz[start: start + qator_hisobi[i]])
        start += qator_hisobi[i]

    result = []
    qator = 0
    qadam = 1
    qator_indeks = [0] * son
    for i in range(n):
        result.append(qatorlar2[qator][qator_indeks[qator]])
        qator_indeks[qator] += 1
        if qator == 0:
            qadam = 1
        elif qator == son - 1:
            qadam = -1
        qator += qadam
    print(qatorlar2)
    return "".join(result)

print(encode("hello world", 3))
print(encode("python programming", 4))
print(encode("zigzag", 5))

print(decode("holelwrdlo", 3))
print(decode("ppmynramtoorighgn", 4))
print(decode("zigzga", 5))








# 3) shifrlash code

def encode(kalit, habar):
    alphabit = 'abcdefghijklmnopqrstuvwxyz'
    shifr = (kalit * (len(habar) // len(kalit) + 1))[:len(habar)]
    javob = []
    for harf in range(len(habar)):
        if habar[harf] in alphabit:
            index = alphabit.index(habar[harf])
            kalit_index = alphabit.index(shifr[harf])
            javob_index = (index + kalit_index) % 26
            javob.append(alphabit[javob_index])
        else:
            javob.append(habar[harf])

    return ''.join(javob)


# Misol uchun
key = "kalit"
message = "helloworld"
javob = encode(key, message)
print(javob)





def decode(encoded_soz, son):
    if son == 1:
        return encoded_soz  # No decoding necessary if only one rail

    n = len(encoded_soz)
    # Step 1: Calculate how many characters each rail has
    qator_hisobi = [0] * son
    qator = 0
    qadam = 1

    for i in range(n):
        qator_hisobi[qator] += 1
        if qator == 0:
            qadam = 1
        elif qator == son - 1:
            qadam = -1
        qator += qadam

    # Step 2: Split the encoded string into the rails
    qatorlar2 = []
    start = 0
    for count in qator_hisobi:
        qatorlar2.append(encoded_soz[start:start + count])
        start += count

    # Step 3: Construct the decoded string
    result = []
    qator = 0
    qadam = 1
    qator_indeks = [0] * son

    for i in range(n):
        result.append(qatorlar2[qator][qator_indeks[qator]])
        qator_indeks[qator] += 1
        if qator == 0:
            qadam = 1
        elif qator == son - 1:
            qadam = -1
        qator += qadam

    return "".join(result)

# Testing the decode function with encoded strings
print(decode("holelwrdlo", 3))             # Output: "hello world"
print(decode("ppmynramtoorighgn", 4))      # Output: "python programming"
print(decode("zigzga", 5))                  # Output: "zigzag"
