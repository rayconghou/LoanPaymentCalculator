def toInt(s):

    isAValidNumber = True

    if len(s) == 0:

        isAValidNumber = False

    else:

        for ch in s:

            if ch not in '0123456789':
                
                isAValidNumber = False

                break
            
        if isAValidNumber == True:

            x = float(s)

    return isAValidNumber

def toReal(s):

    isAValidNumber = True

    if len(s) == 0:

        isAValidNumber = False

    else:

        for ch in s:

            if ch not in '0123456789.':
                
                isAValidNumber = False

                break

        n = 0

        for ch in s:

            if ch == '.':

                n += 1

                if n > 1:
                    isAValidNumber = False
                    break
            
        if isAValidNumber == True:

            x = float(s)

    return isAValidNumber

# test code

if __name__ == '__main__':

    test_data = ['1.234', '1.234a', '1.23.4', \
                 '', '123', 'a123']

    for s in test_data:

        # check if s can be converted to an int

        result = toInt(s)

        # print result

        print('\'{}\' can be convered to an int: {}'.format(s, result))

        # check if s can be converted to an int

        result = toReal(s)

        # print result

        print('\'{}\' can be converted to a real: {}'.format(s, result))

        print()









