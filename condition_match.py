message = input('ENTER MSG :')

match message:
    case 'Hello':
        print('Hi')
    case 'Bye':
        print("Good night")
    case 'Ok':
        print('Cool')
    case other:
        print('Nothing to say about')

# using if
if message == 'Hello':
    print('Hi')
elif message == 'Bye':
    print("Good night")
elif message == 'Ok':
    print('Cool')
else:
    print('Nothing to say about')