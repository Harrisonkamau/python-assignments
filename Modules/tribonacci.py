from user import enter_num # import module


def tribo(n):
    n = enter_num
    queue = [1, 1, 1]
    for i in xrange(n - 2):
        queue = queue[1:] + [sum(queue)]
    return queue[-1]


print ("Tribonacci for 4 is {}".format(tribo(4)))
