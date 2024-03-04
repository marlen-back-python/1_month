'''CHARACTERS'''
characters = ['Kiyotaka', 'Manabu', 'Nagumo']
print(characters)
print('(add) (edit) (delete) (exit)')
while True:
    what = input('What do you want to do?: ')
    if what == 'add':
        new_name = input('Enter name: ').title()
        if new_name not in characters:
            if len(new_name) <= 15:
                characters.append(new_name)
            else:
                print('This name is too long! letters should not exceed 15')
        else:
            print('This name is already in the list!')
    if what == 'edit':
        change_name = input("Who be replaced?: ").title()
        if change_name in characters:
            newname = input("Who to replace with?: ").title()
            if newname not in characters:
                if len(newname) <= 15:
                    characters[characters.index(change_name)] = newname
                else:
                    print('This name is too long! letters should not exceed 15')
            else:
                print('This name is already on the list! Choose another')
        else:
            print('This name is not on the list!')
    elif what == 'delete':
        how = input('Delete by number or by letter?: ')
        if how == 'number':
            try:
                ind = int(input('Who be removed?: '))
                if ind <= len(characters) - 1 and ind >= 0:
                    characters.pop(ind)
            except:
                print('Please enter "number(int)"!!!')
        elif how == 'letter':
            value = input('Who be removed?: ').title()
            if value in characters:
                characters.remove(value)
            else:
                print('Please enter "letter(str)"!!!')
        else:
            print('Enter the command you choose!')
    elif what == 'exit':
        break
    else:
        print('There are only 4 commands: (add) (edit) (delete) (exit)')
    print(characters)
    print(tuple(characters))