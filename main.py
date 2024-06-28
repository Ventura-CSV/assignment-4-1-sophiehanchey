def main():
    result = []
    start = input('Enter the starting letter: ').lower()
    end = input('Enter the ending letter: ').lower()
        
     # check input is letters
    while start.isalpha() == False:
        start = input('Please enter a letter for the start: ').lower()
        
    while end.isalpha() == False:
        end = input('Please enter a letter for the end: ').lower()
        
    # check order is correct    
    while ord(start) >= ord(end):
        end = input(f'Please enter a letter that comes after {start}: ')    

    # create the list
    for i in range(ord(start), ord(end +1)):
        newlet = chr(ord(start) + i)
        result.append(newlet)
    
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
