
def symmetry_check(num: int) -> bool:
    """
        дано число, надо определить является ли оно симметричным ? (1221 - симметричное , 123 - не симметричное )
    """
    num_str = str(num)
    if len(num_str) == 1 or len(num_str) == 2:
        return False

    first_part = num_str[:len(num_str)//2]

    if len(num_str) % 2 == 0:
        second_part = num_str[len(num_str)//2:]
    else:
        second_part = num_str[len(num_str)//2 + 1:]

    return first_part == second_part[::-1]


print(symmetry_check(222345))
print(symmetry_check(2224345))
print(symmetry_check(222434595418081))
print(symmetry_check(1221))
print(symmetry_check(1224221))
print(symmetry_check(123454321))
