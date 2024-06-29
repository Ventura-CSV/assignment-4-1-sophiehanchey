def main():
    result = []

    start = ''
    end = ''
    isAlpha1 = False
    isAlpha2 = False
    isOrd = False
    
    while not(isAlpha1 and isAlpha2 and isOrd):
        #ask for first letter
        start = input('Please enter a letter for the start: ').lower()
        isAlpha1 = start.isalpha()

        # asking for input
        end = input(f'Please enter a letter for the end that comes after {start}: ' ).lower()
        
        # evaluate two conditions
        isAlpha2 = end.isalpha()
        if isAlpha1 and isAlpha2: 
            ordstart = ord(start)
            ordend = ord(end)
            isOrd = ordend >= ordstart

    # create the list
    for i in range(ord(start), ord(end) + 1):
        newlet = chr(i)
        result.append(newlet)
    
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
