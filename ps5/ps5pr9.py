# PS5 Problem 8
#
# Choosing the correct type of loop
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu

def add_odds(n):
    """takes a non-negative integer n and that uses a loop to
    compute and return the sum of the first n positive odd integers"""

    odd_sum = 0
    curr_odd = 1

    for i in range(n):
        curr_sum = odd_sum + curr_odd
        print(f"{odd_sum} + {curr_odd} = {curr_sum}")
        odd_sum += curr_odd
        curr_odd += 2

    return odd_sum


def largest_pow2(n):
    """takes a positive integer n and that uses
    a loop to find and return the largest power of
    2 that is less than or equal to n"""

    pow_num = 1
    sum_num = 0
    print("2 ** 0 = 1")

    while 2 ** pow_num <= n:
        sum_num = 2 ** pow_num
        pow_num += 1
        print(f"2 ** {pow_num - 1} = {sum_num}")

    return_statement = 2 ** (pow_num - 1)
    sum_num = 2 ** pow_num
    pow_num += 1
    print(f"2 ** {pow_num - 1} = {sum_num}")

    return return_statement


def test():
    """tests functions made"""

    # add_odds()
    print(f"add_odds(5):  {add_odds(5)}\n")
    print(f"add_odds(3):  {add_odds(3)}\n")
    print(f"add_odds(7):  {add_odds(7)}\n")
    print(f"add_odds(0):  {add_odds(0)}\n")

    # largest_pow2()
    print(f"largest_pow2(18):  {largest_pow2(18)}\n")
    print(f"largest_pow2(8):  {largest_pow2(8)}\n")
    print(f"largest_pow2(1):  {largest_pow2(1)}\n")
    print(f"largest_pow2(150):  {largest_pow2(150)}\n")


test()
