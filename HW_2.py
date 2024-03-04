'''13 ZODIAC SIGNS ACCORDING TO SCIENTIFIC RESEARCH 15/11/2018'''
print()
print('13 ZODIAC SIGNS ACCORDING TO SCIENTIFIC RESEARCH 15/11/2018')

while True:
    ask = input("Start?: ")
    if ask == "no":
        print("Okay")
        break
    elif ask == "yes":
        birth = int(input('Enter your birthday: '))
        month = int(input('Enter month of birth: '))

        if (month == 1 and 19 <= birth <= 31) or (month == 2 and 1 <= birth <= 15):
            print('Your zodiac sign is: "Capricorn"')

        elif (month == 2 and 16 <= birth <= 29) or (month == 3 and 1 <= birth <= 11):
            print('Your zodiac sign is: "Aquarius"')
        elif (month == 3 and 12 <= birth <= 31) or (month == 4 and 1 <= birth <= 18):
            print('Your zodiac sign is: "Pisces"')
        elif (month == 4 and 19 <= birth <= 30) or (month == 5 and 1 <= birth <= 13):
            print('Your zodiac sign is: "Aries"')
        elif (month == 5 and 14 <= birth <= 31) or (month == 6 and 1 <= birth <= 19):
            print('Your zodiac sign is: "Taurus"')
        elif (month == 6 and 20 <= birth <= 30) or (month == 7 and 1 <= birth <= 20):
            print('Your zodiac sign is: "Gemini"')
        elif (month == 7 and 21 <= birth <= 31) or (month == 8 and 1 <= birth <= 9):
            print('Your zodiac sign is: "Cancer"')
        elif (month == 8 and 10 <= birth <= 31) or (month == 9 and 1 <= birth <= 15):
            print('Your zodiac sign is: "Leo"')
        elif (month == 9 and 16 <= birth <= 30) or (month == 10 and 1 <= birth <= 30):
            print('Your zodiac sign is: "Virgo"')
        elif (month == 10 and birth >= 31) or (month == 11 and 1 <= birth <= 22):
            print('Your zodiac sign is: "Libra"')
        elif (month == 11 and birth >= 23) or (month == 11 and 1 <= birth <= 29):
            print('Your zodiac sign is: "Scorpio"')
        elif (month == 11 and 30 <= birth <= 31) or (month == 12 and 1 <= birth <= 17):
            print('Your zodiac sign is: "Ophiuchus"')
        elif (month == 12 and 18 <= birth <= 31) or (month == 1 and 1 <= birth <= 18):
            print('Your zodiac sign is: "Sagittarius"')

        else:
            print('You entered the wrong date!')
    else:
        print('Please write either "no" or "yes"')