'''VOWEL & CONSONANT COUNTER'''
print()
print('VOWEL & CONSONANT COUNTER')
vowels = ('йуеыаоэяиюeyuioa')
consonants = ('цкнгшщзхфвпрлджчсмтбqwrtpsdfghjklzxcvbnm')
while True:
    word1 = input('\nEnter your word: ')
    word = word1.lower()
    if word == 'Exit':
        print('Okay')
        break
    count_letter = 0
    count_vowels = 0
    count_consonants = 0
    for i in word:
        if i in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
        count_letter += 1
    avg_vowels = round(count_vowels * 100 / count_letter, 2)
    avg_consonants = round(count_consonants * 100 / count_letter, 2)
    #print(f'Your word: {word1}')
    print(f"Number of letters: {count_letter}")
    print(f"Number of vowels: {count_vowels}")
    print(f"Number of consonants: {count_consonants}")
    print(f"Consonants & Vowels: {avg_consonants} & {avg_vowels}")
