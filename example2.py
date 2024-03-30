

def find_third_max_element(list1: list) -> int:
    """
        Реализуй алгоритм, для поиска 3-его максимального
        элемента (бронза) + выпиши сложность.
    """
    max1 = 0
    i = 0
    while i <= len(list1) - 1:
        if max1 < list1[i]:
            max1 = list1[i]
        
        i += 1
    
    max2 = 0
    i = 0
    while i <= len(list1) - 1:
        if max2 < list1[i] < max1:
            max2 = list1[i]
        
        i += 1
    
    
    max3 = 0
    i = 0
    while i <= len(list1) - 1:
        if max3 < list1[i] < max2 < max1:
            max3 = list1[i]
        
        i += 1
    
    
    
    return max3
        


list1 = [3, 1, 6, 5, 2, 4] # -> вывести 4
list2 = [38, 42, 33, 71, 3, 21, 77, 99, 59, 63] # -> вывести 71
list3 = [22, 100, 12, 41, 85, 79, 92, 79, 92, 89, 72, 34, 89, 44, 10] # -> вывести 89
print(find_third_max_element(list1))