from user import enter_num # import module


def tribo(n):
    # maximum recussion error for 4000
    n = enter_num
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)

print tribo(6)
