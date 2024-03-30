

def solution_fast(list1: list, target: int) -> bool:
    """
      1. Реализуй solution_fast (поиск элемента в массиве с двух сторон за итерацию)
    """
    i = 0
    j = len(list1) - 1
    while i <= j:
        left_value = list1[i]
        right_value = list1[j]
        
        print(left_value, " -- ", right_value)
        
        if left_value == target or right_value == target:
            return True
        
        i = i + 1
        j = j - 1
        
    
#     for i in range(len(list1)):
#         left_value = list1[0 + i]
#         right_value = list1[high - i]
#         
#         print(left_value, " -- ", right_value)
#         
#         if left_value == target or right_value == target:
#             find = True
#             break
    
    return False
    
#list1 = [2, 45, 86, 43, 20, 20, 47]
# list1 = [38, 42, 33, 71, 3, 21, 77, 99, 59, 63]
list1 = [4728, 982, 902]
# list1 = [22, 100, 12, 41, 85, 79, 92, 79, 92, 89, 72, 34, 89, 44, 10]
print(solution_fast(list1, 53))

