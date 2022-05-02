import os

masterlist = []
list1 = []
list2 = []
list3 = []
list4 = []

def main():
    os.system('cls')
    input('Press Enter')
    themain()

def themain():
    while True:
        choices = ['1', '2', '3', '4', '5', '6', '7']
        choices2 = ['1', '2', '3', '4', '5', '6']

        def add1():
            input('\nadded thing1 to list1')
            list1.append('thing1')
            masterlist.append('thing1')
        def add2():
            input('\nadded thing2 to list2')
            list2.append('thing2')
            masterlist.append('thing2')
        def add3():
            input('\nadded thing3 to list3')
            list3.append('thing3')
            masterlist.append('thing3')
        def add4():
            input('\nadded thing1 and thing2 to list4')
            list4.append('thing1, thing2')
            masterlist.append('thing1, thing2')
        def do5things():
            print('\nMasterlist: ', masterlist)
            print('List1: ', list1)
            print('List2: ', list2)
            print('List3: ', list3)
            print('List4: ', list4)
            input()
        def do6things():
            while True:
                os.system('cls')
                def del1():
                    try:
                        print('\nList1:')
                        for index, value in enumerate(list1):
                            print((index, value))
                        choice3 = input('\ndelete: ')
                        try:
                            if len(list1) == 0:
                                raise ValueError
                            else:
                                input('deleted')
                                choice3 = int(choice3)
                                list1.pop(choice3)
                                K = 'thing1'
                                if(K in masterlist):
                                    masterlist.remove(K)
                                return do6things()
                        except ValueError or IndexError or SyntaxError:
                            input('\nwrong')
                            return do6things()
                    except ValueError or IndexError or SyntaxError:
                        input('\nwrong')
                        return do6things()

                def del2():
                    try:
                        print('\nList2:')
                        for index, value in enumerate(list2):
                            print((index, value))
                        choice4 = input('\ndelete: ')
                        try:
                            if len(list2) == 0:
                                raise ValueError
                            else:
                                input('deleted')
                                choice4 = int(choice4)
                                list2.pop(choice4)
                                W = 'thing2'
                                if(W in masterlist):
                                    masterlist.remove(W)
                                return do6things()
                        except ValueError or IndexError or SyntaxError:
                            input('\nwrong')
                            return do6things()
                    except ValueError or IndexError or SyntaxError:
                        input('\nwrong')
                        return do6things()

                def del3():
                    try:
                        print('\nList3:')
                        for index, value in enumerate(list3):
                            print((index, value))
                        choice5 = input('\ndelete: ')
                        try:
                            if len(list3) == 0:
                                raise ValueError
                            else:
                                input('deleted')
                                choice5 = int(choice5)
                                list3.pop(choice5)
                                X = 'thing3'
                                if(X in masterlist):
                                    masterlist.remove(X)
                                return do6things()
                        except ValueError or IndexError or SyntaxError:
                            input('\nwrong')
                            return do6things()
                    except ValueError or IndexError or SyntaxError:
                        input('\nwrong')
                        return do6things()

                def del4():
                    try:
                        print('\nList4:')
                        for index, value in enumerate(list4):
                            print((index, value))
                        choice6 = input('\ndelete: ')
                        try:
                            if len(list4) == 0:
                                raise ValueError
                            else:
                                input('deleted')
                                choice6 = int(choice6)
                                list4.pop(choice6)
                                Y = 'thing1, thing2'
                                if(Y in masterlist):
                                    masterlist.remove(Y)
                                return do6things()
                        except ValueError or IndexError or SyntaxError:
                            input('\nwrong')
                            return do6things()
                    except ValueError or IndexError or SyntaxError:
                        input('\nwrong')
                        return do6things()

                def delmaster():
                    try:
                        print('\nMasterList:')
                        for index, value in enumerate(masterlist):
                            print((index, value))
                        choice7 = input('\ndelete: ')
                        try:
                            if len(masterlist) == 0:
                                raise ValueError
                            else:
                                choice7 = int(choice7)
                                item = masterlist[choice7]
                                if item == 'thing1':
                                    if len(list1) == 0:
                                        raise ValueError
                                    else:
                                        list1.pop()
                                elif item == 'thing2':
                                    if len(list2) == 0:
                                        raise ValueError
                                    else:
                                        list2.pop()
                                elif item == 'thing3':
                                    if len(list3) == 0:
                                        raise ValueError
                                    else:
                                        list3.pop()
                                elif item == 'thing1, thing2':
                                    if len(list4) == 0:
                                        raise ValueError
                                    else:
                                        list4.pop()
                                masterlist.pop(choice7)
                                input('deleted')
                                return do6things()
                        except ValueError or IndexError or SyntaxError:
                            input('\nwrong')
                            return do6things()
                    except ValueError or IndexError or SyntaxError:
                        input('\nwrong')
                        return do6things()

                print('\nOpen - ')
                print('1 = list1')
                print('2 = list2')
                print('3 = list3')
                print('4 = list4')
                print('5 = masterlist')
                print('6 = back')
                choice2 = input('\nChoice: ')
                try:
                    if choice2 not in choices2:
                        raise ValueError
                    elif choice2 == '1':
                        del1()
                    elif choice2 == '2':
                        del2()
                    elif choice2 == '3':
                        del3()
                    elif choice2 == '4':
                        del4()
                    elif choice2 == '5':
                        delmaster()
                    elif choice2 == '6':
                        themain()
                except ValueError or IndexError or SyntaxError:
                    input('\nwrong')
                    return do6things()

        os.system('cls')
        print('\nYou can add things to different lists')
        print('and you can delete things')
        print('Which list do you want to add a thing too?')
        print('These are your options...')
        print()
        print('Choose - ')
        print('1 = list1')
        print('2 = list2')
        print('3 = list3')
        print('4 = list4')
        print('5 = see the lists')
        print('6 = delete something')
        print('7 = exit')
        number = str(input('\nChoice: '))
        try:
            if number == '1':
                add1()
            elif number == '2':
                add2()
            elif number == '3':
                add3()
            elif number == '4':
                add4()
            elif number == '5':
                do5things()
            elif number == '6':
                do6things()
            elif number == '7':
                exit()
            if number not in choices:
                raise ValueError
        except ValueError or IndexError or SyntaxError:
            input('\nwrong')
            return themain()

if __name__ == '__main__':
    main()
