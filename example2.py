from mytest import test_func


def find_third_max_element1(list1: list) -> int:
    """
        Реализуй алгоритм, для поиска 3-его максимального
        элемента (бронза) + выпиши сложность.
    """
    if len(list1)<=2:
        return None
    
    i = 1
    while i <= len(list1) - 1:
        if list1[0] < list1[i]:
            list1[0], list1[i] = list1[i], list1[0]
            
        i += 1
    
    i = 2
    while i <= len(list1) - 1:
        if list1[1] < list1[i] and list1[1] != list1[i]:
            list1[1], list1[i] = list1[i], list1[1]
        
        i += 1
    
    i = 3
    while i <= len(list1) - 1:
        if list1[2] < list1[i] and list1[1] != list1[i]:
            list1[2], list1[i] = list1[i], list1[2]
        
        i += 1

    return list1[2]


def find_third_max_element2(list1: list) -> int:
    """
        Реализуй алгоритм, для поиска 3-его максимального
        элемента (бронза) + выпиши сложность.
    """
    pass

test_func(find_third_max_element1)


list1 = [12, 84, -7, -13, 0, 321]
print(find_third_max_element1(list1))



