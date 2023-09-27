def count_in_list(lst, item):
    ''''
    count the number of the input string present in the list
    '''
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count
