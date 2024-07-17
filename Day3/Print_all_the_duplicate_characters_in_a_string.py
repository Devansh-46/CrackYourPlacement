def printDuplicates(str):

    char_list = list(str)

    char_list.sort()
    
    i = 0
    while i < len(char_list):
        count = 1

        while i < len(char_list)-1 and char_list[i] == char_list[i+1]:
            count += 1
            i += 1
        
        if count > 1:
            print(char_list[i], ", count = ", count)
        i += 1

str = "test string"
printDuplicates(str)
