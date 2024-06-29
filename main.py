def main():
    result = []
   
    #check that each input is a letter 
    start = ''
    while not start.isalpha():
        start = input('Please enter a letter for the start: ').lower()
    
    ordstart = ord(start)

    end = ''
    isAlpha = False
    isOrd = False
    while not(isAlpha and isOrd):
        # choose the prompt based on latest input
        if not isAlpha:
            prompt = 'Please enter a letter for the end: '        
        else:
            prompt = f'Please enter a letter that comes after {start}'
        
        # asking for input
        end = input(prompt).lower()
        
        # evaluate two conditions
        isAlpha = end.isalpha()
        if isAlpha: 
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
