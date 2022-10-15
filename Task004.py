# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open('codedtext.txt', 'r') as data:
    my_text = data.read()


def encode_text(text):
    encoding = "" 
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + text[i]
        i = i + 1
 
    return encoding
        
encoding = encode_text(my_text)
print(encoding)

with open('uncodingtext.txt', 'r') as data:
    my_text2 = data.read()

def decoding_text(text:str):
    count = ''
    decoding = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            decoding += str(int(count) * i)
            count = ''
    return decoding

decoding = decoding_text(my_text2)
print(decoding)