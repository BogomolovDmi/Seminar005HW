# Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

my_text = 'Напишите программу, удаляющую ыыыабвыыы из текста лишниабвы все слова абвбус содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)